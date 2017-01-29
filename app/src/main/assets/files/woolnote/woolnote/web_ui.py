# TODO: think about moving functionality to backend

import urllib
import re
import hashlib

from woolnote import util
from woolnote import config
from woolnote.html_page_templates import edit_note_page_template, template_page_list_notes # TODO fix this
from woolnote import html_page_templates
from woolnote import html_constants
from woolnote.task_store import Task, TaskStore, PLAIN, MARKUP


# Web UI frontend
#################

class WebUI():
    def __init__(self, task_store, task_store_trash, ui_backend, woolnote_config, ui_auth):
        # TODO: docstring

        # history_back gets the proper history hash (history_id) so that it uses that instead
        self.last_request_post_data_dict = {}
        self.last_request_get_dict = {}
        self.error_msg_queue_list = []  # error messages to be displayed on a task list
        self.error_msg_queue_note = []  # error messages to be displayed on a note

        # history of visited paths so that a "back" link can be provided
        self.last_history_dict_of_links = {}

        # this is used for permanent actions like delete so that get requests with permanent effects cannot be cached and mistakenly used in other sessions
        self.sess_action_auth = util.create_id_task()  # create a new random auth string

        # this is used for permanent actions like import/export so that get requests with permanent effects cannot be cached and mistakenly used in other sessions or by going back in the browser's history
        self.nonce_action_auth = util.create_id_task()  # create a new random auth string
        self.nonce_action_auth_valid_uses = 0  # do not allow the value to be used at beginning

        self.task_store = task_store
        self.task_store_trash = task_store_trash
        self.ui_backend = ui_backend
        self.woolnote_config = woolnote_config
        self.ui_auth = ui_auth
        super().__init__()

    def set_last_request(self, postdict, getdict):
        # TODO docstring
        # - to be used by the http request handler before calling any methods for a new request
        self.last_request_post_data_dict = postdict
        self.last_request_get_dict = getdict

    def get_last_request_from_history_id(self, id):
        # TODO docstring
        # - to be used by the http request handler to go back in request history
        return self.last_history_dict_of_links[id].copy()

    def save_history(self, req_keys_to_save, alt_task_store_name=None):
        # TODO docstring
        # - to be used by the other methods in this class - the methods that display a listing of notes, so that notes can go back to the same listing
        history_id = "main_list"  # fallback string
        _hd = self.last_request_get_dict
        _hk = req_keys_to_save
        _lhgd = {k: _hd[k] for k in _hd if k in _hk}
        if _lhgd:
            if alt_task_store_name is not None:
                _lhgd.update({"alt_task_store_name": [alt_task_store_name]})
            # save only if the dict is nonempty, so that favicon.ico does not overwrite it
            history_id = hashlib.sha256(repr(_lhgd).encode("utf-8")).hexdigest()
            self.last_history_dict_of_links[history_id] = _lhgd
        return history_id

    def helper_convert_msg_queue_list_to_list_for_output(self):
        # TODO: docstring
        # docstr: creates a new static list of warning collected so far, empties the list, does all that in a cooperative multitasking-safe way
        result = []
        if self.error_msg_queue_list:
            # this order of reference shuffling ensures that a race condition doesn't result in lost messages
            msg_list = self.error_msg_queue_list
            self.error_msg_queue_list = []
            result = [str(x) for x in msg_list]
        return result

    def helper_convert_msg_queue_note_to_list_for_output(self):
        # TODO: docstring
        # docstr: creates a new static list of warning collected so far, empties the list, does all that in a cooperative multitasking-safe way
        result = []
        if self.error_msg_queue_note:
            # this order of reference shuffling ensures that a race condition doesn't result in lost messages
            msg_list = self.error_msg_queue_note
            self.error_msg_queue_note = []
            result = [str(x) for x in msg_list]
        return result


    def helper_sessactionauth_is_wrong(self):
        """
        Gets the GET value sessactionauth and finds out whether it is wrong

        Returns:
            bool: True if sessactionauth is wrong
        """
        wrong = not util.safe_string_compare(self.sess_action_auth, self.last_request_get_dict["sessactionauth"][0])
        if wrong:
            util.dbgprint("sessactionauth is wrong - {}".format(self.last_request_get_dict["sessactionauth"][0]))
        return wrong

    def helper_action_get_request_is_wrong(self, action_name):
        """
        Gets the GET value "action" and finds out whether it is wrong
        Throws an exception if the data don't exist so that the exception bubbles up.

        Args:
            action_name (string): The action string that is expected to be right

        Returns:
            bool: True if the provided action name and the contents of the action dictionary key differ
        """
        wrong = not util.safe_string_compare(action_name, self.last_request_get_dict["action"][0])
        return wrong

    def helper_action_post_request_is_wrong(self, action_name, dict_key=None):
        """
        Gets the POST value "action" and finds out whether it is wrong
        Doesn't throw an exception if the data don't exist becacuse it is sometimes expected that they don't and so
        it just returns True.

        Args:
            action_name (string): The action string that is expected to be right
            dict_key (string): Alternative dictionary string to use (instead of "action")

        Returns:
            bool: True if the provided action name and the contents of the action dictionary key differ or if the dict key doesn't exist.
        """
        try:
            if dict_key is None:
                dict_key = "action"
            wrong = not util.safe_string_compare(action_name, self.last_request_post_data_dict[dict_key][0])
            return wrong
        except:
            return True

    def helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none(self, key_name):
        # TODO: docstring
        # docstr: returns either the first GET value of the specified key or (if it doesnt exist) None
        try:
            return self.last_request_get_dict[key_name][0]
        except:
            return None

    def create_new_nonce(self):
        # TODO docstring
        """Creates a new nonce and sets how many tries are left (just one try). To be used for pages whose actions must not be repeated by reloading the page / resending the request."""
        self.nonce_action_auth = util.create_id_task()  # create a new random auth string
        self.nonce_action_auth_valid_uses = 1
        return self.nonce_action_auth

    def check_one_time_pwd(self, user_supplied_nonce):
        # TODO docstring
        x = """Checks whether the supplied nonce is correct, only if tries are left.
            Nonce is disabled after 1st successful use.
To be used for pages whose actions must not be repeated by reloading the page / resending the request.
        """
        if self.nonce_action_auth_valid_uses > 0:
            self.nonce_action_auth_valid_uses -= 1
            ret = util.safe_string_compare(user_supplied_nonce, self.nonce_action_auth)
            if ret is True:  # explicitly checking for boolean True
                return True
            return False
        return False

    def helper_get_alt_task_store_name(self):
        #TODO docstring
        # docstr: returns alt_task_store_name if present in the get data or None if not present
        return self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("alt_task_store_name")

    def req_display_otp(self):
        """
        Puts a new generated one-time password to the self.error_msg_queue_list so that it is displayed.
        """

        ret = self.ui_auth.create_new_one_time_pwd()
        if ret is not None:
            self.error_msg_queue_list.append(ret)

    def helper_save_note(self, task):
        # TODO: docstring
        # TODO: somehow move validation to ui_backend?
        # docstr: reads data for a new/saved note from POST data, performs sanitization, and correctly saves the data to a note (that also entails resetting the reminder flag if due date changes, correctly processing body text based on formatting used, setting the correct values for the formatting property)
        tainted_task_name = self.last_request_post_data_dict.get("taskname", [config.DEFAULT_TASKNAME])[0]
        tainted_task_folder = self.last_request_post_data_dict.get("taskfolder", [config.DEFAULT_FOLDER])[0]
        tainted_task_pubauthid = self.last_request_post_data_dict.get("taskpubauthid", [util.create_id_task()])[0]
        tainted_task_tags = self.last_request_post_data_dict.get("tasktags", [""])[0]
        if tainted_task_tags.endswith(", "):
            tainted_task_tags = tainted_task_tags[:-2]
        tainted_task_body = self.last_request_post_data_dict.get("taskbody", [""])[0]
        tainted_due_date = self.last_request_post_data_dict.get("duedate", [""])[0]
        tainted_formatting = self.last_request_post_data_dict.get("formatting", ["markup"])[0]

        task.name = util.sanitize_singleline_string_for_tasksave(tainted_task_name)
        task.folder = util.sanitize_singleline_string_for_tasksave(tainted_task_folder)
        task.tags = {util.sanitize_singleline_string_for_tasksave(x) for x in tainted_task_tags.split(",")}

        old_due_date = task.due_date
        task.due_date = util.sanitize_singleline_string_for_tasksave(tainted_due_date)
        if old_due_date != task.due_date:
            # when due date changes, the note is again ready to display a red reminder
            task.due_date_reminder_dismissed = False

        task.public_share_auth = util.sanitize_singleline_string_for_tasksave(tainted_task_pubauthid)
        # too short strings are inherently insecure
        if len(task.public_share_auth) < 5:
            task.public_share_auth = util.create_id_task()

        if tainted_formatting == "markup":
            task.body_format = MARKUP
        elif tainted_formatting == "plaintext":
            task.body_format = PLAIN
        else:
            # keeping unchanged, shouldn't happen
            util.dbgprint("tainted_formatting had a nonstandard value {}".format(tainted_formatting))
            pass

        if task.body_format == MARKUP:
            task.body = util.task_body_save_fix_multiline_markup_bullet_lists(tainted_task_body)
        else:
            task.body = util.task_body_save_fix_newlines(tainted_task_body)

    def req_save_new_note(self):
        # TODO: docstring
        """
        Saves a new note from the GET and POST data.
        Has a permanent effect - calls task_store.task_store_save()
        """

        if self.helper_action_get_request_is_wrong("req_save_new_note"):
            return

        if self.helper_sessactionauth_is_wrong():
            return

        task = Task()

        self.helper_save_note(task)

        self.ui_backend.save_new_note_permanent(task)
        self.last_request_get_dict["taskid"] = [
            task.taskid]  # inject back so that the next rendered page can access it as if the note always existed

    def req_save_edited_note(self):
        # TODO: docstring
        # TODO prevent user setting/fixing the note id - if it doesnt exist, do not save
        """
        Saves a new version of an existing note from the GET and POST data.
        Has a permanent effect - calls task_store.task_store_save()
        """

        if self.helper_action_get_request_is_wrong("req_save_edited_note"):
            self.error_msg_queue_note.append("Note has not been saved.")
            return

        if self.helper_action_post_request_is_wrong("req_save_edited_note", "post_action"):
            # this POST value is not present when the page is visited from history
            # missing POST data and not doing this check would delete all checkboxes on the page
            self.error_msg_queue_note.append("Note has not been saved - wrong request (page reload?).")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_note.append("Note has not been saved - wrong session.")
            return

        task_id = util.sanitize_singleline_string_for_tasksave(self.last_request_get_dict["taskid"][0])
        task = self.task_store.store_dict_id[task_id]

        self.helper_save_note(task)

        self.ui_backend.save_edited_note_permanent(task)

    def req_note_dismiss_reminder(self):
        # TODO: docstring
        if self.helper_action_get_request_is_wrong("dismiss_reminder_and_display_note"):
            self.error_msg_queue_note.append("Reminder has not been dismisses - application error?")
            return

        task_id = util.sanitize_singleline_string_for_tasksave(self.last_request_get_dict["taskid"][0])
        task = self.task_store.store_dict_id[task_id]

        # TODO move to backend?
        task.due_date_reminder_dismissed = True
        self.task_store.task_store_save()

    def req_note_checkboxes_save(self):
        # TODO: docstring
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        if self.helper_action_get_request_is_wrong("req_note_checkboxes_save"):
            self.error_msg_queue_note.append("Checkboxes were not saved.")
            return

        if self.helper_action_post_request_is_wrong("req_note_checkboxes_save", "post_action"):
            # this POST value is not present when the page is visited from history
            # missing POST data and not doing this check would delete all checkboxes on the page
            self.error_msg_queue_note.append("Checkboxes were not saved - wrong request (page reload?).")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_note.append("Checkboxes were not saved - wrong session.")
            return

        task_id = util.sanitize_singleline_string_for_tasksave(self.last_request_get_dict["taskid"][0])
        task = self.task_store.store_dict_id[task_id]

        hash_task_body_current = hashlib.sha256(repr(task.body).encode("utf-8")).hexdigest()
        hash_task_body_request = self.last_request_get_dict.get("task_body_hash", [""])[0]
        if hash_task_body_current != hash_task_body_request:
            self.error_msg_queue_note.append("Checkboxes were not saved - tried to save checkboxes for an older version of the note.")
            return

        post_data_keys = list(self.last_request_post_data_dict.keys())
        cms_str = util.convert_multiline_markup_string_into_safe_html(task.body)
        new_task_body = util.multiline_markup_checkbox_mapping(cms_str, task.body, edit_chkbox_state=True,
                                                               chkbox_on_list=post_data_keys)

        task.body = new_task_body
        self.ui_backend.save_edited_note_permanent(task)

    def req_import_notes_permanent(self):
        # TODO: docstring
        """
        Has a potentially permanent effect - imports notes that may be saved via task_store.task_store_save() on next operation, imports database
        """

        if self.helper_action_get_request_is_wrong("req_import_notes_permanent"):
            self.error_msg_queue_list.append("Import not performed.")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Import not performed - wrong session?")
            return

        user_supplied_nonce = self.last_request_get_dict["nonceactionauth"][0]
        if not self.check_one_time_pwd(user_supplied_nonce):
            self.error_msg_queue_list.append("Import not performed - page expired.")
            return

        replace_local_request = "yes" == self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("replace_local")

        ret = self.ui_backend.import_notes_permanent(replace_local_request)
        if ret is not None:
            self.error_msg_queue_list.append(ret)

    def req_export_notes_permanent(self):
        # TODO: docstring
        """
        Has a permanent effect - calls task_store.task_store_save(), exports database
        """

        if self.helper_action_get_request_is_wrong("req_export_notes_permanent"):
            self.error_msg_queue_list.append("Export not performed.")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Export not performed - wrong session?")
            return

        user_supplied_nonce = self.last_request_get_dict["nonceactionauth"][0]
        if not self.check_one_time_pwd(user_supplied_nonce):
            self.error_msg_queue_list.append("Export not performed - page expired.")
            return

        self.ui_backend.export_notes_permanent()

    def req_delete_taskid_permanent(self):
        # TODO: docstring
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        if self.helper_action_get_request_is_wrong("req_delete_taskid_permanent"):
            self.error_msg_queue_list.append("Note deletion not performed.")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Note deletion not performed - wrong session?")
            return

        task_id_list = self.last_request_post_data_dict["taskid"]
        self.ui_backend.delete_taskid_permanent(task_id_list)

    def req_note_list_manipulate_tagdel(self):
        # TODO: docstring
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        if self.helper_action_get_request_is_wrong("req_note_list_manipulate_tagdel"):
            self.error_msg_queue_list.append("Note manipulation not performed.")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Note manipulation not performed - wrong session?")
            return

        try:
            task_id_list = self.last_request_post_data_dict["taskid"]
            tagdel = self.last_request_post_data_dict["tagdel"][0]
        except:
            self.error_msg_queue_list.append("Note manipulation not performed - cannot access required POST data.")
        else:
            self.ui_backend.notes_tagdel_permanent(task_id_list, tagdel)
            self.task_store.task_store_save()

    def req_note_list_manipulate_tagadd(self):
        # TODO: docstring
        """
        Has a permanent effect - calls task_store.task_store_save()
        """

        if self.helper_action_get_request_is_wrong("req_note_list_manipulate_tagadd"):
            self.error_msg_queue_list.append("Note manipulation not performed.")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Note manipulation not performed - wrong session?")
            return

        try:
            task_id_list = self.last_request_post_data_dict["taskid"]
            tagadd = self.last_request_post_data_dict["tagadd"][0]
        except:
            self.error_msg_queue_list.append("Note manipulation not performed - cannot access required POST data.")
        else:
            self.ui_backend.notes_tagadd_permanent(task_id_list, tagadd)
            self.task_store.task_store_save()

    def req_note_list_manipulate_foldermove(self):
        # TODO: docstring
        """
        Has a permanent effect - calls task_store.task_store_save()
        """

        if self.helper_action_get_request_is_wrong("req_note_list_manipulate_foldermove"):
            self.error_msg_queue_list.append("Note manipulation not performed.")
            return

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Note manipulation not performed - wrong session?")
            return

        try:
            task_id_list = self.last_request_post_data_dict["taskid"]
            foldermove = self.last_request_post_data_dict["foldermove"][0]
        except:
            self.error_msg_queue_list.append("Note manipulation not performed - cannot access required POST data.")
        else:
            self.ui_backend.notes_foldermove_permanent(task_id_list, foldermove)
            self.task_store.task_store_save()

    def helper_get_task_or_default(self):
        """
        A helper function that either retrieves the requested task from the request or returns contents of a page
        that should be rendered when the task has not been found in the request.

        Returns:
            Union[Tuple[bool, str, woolnote.task_store.Task, str], Tuple[bool, int, int, str]]:
            1) bool - whether a task specified by "taskid" in request was found
            2) the taskid of the task, if found
            3) the task, if found
            4) the "not found" page that should be rendered if task not found
        """
        task_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("taskid")
        alt_task_store_name = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("alt_task_store_name")
        used_task_store = self.task_store
        # don't want to use sth like globals.get(alt_task_store) so that only approved stores can be used
        if alt_task_store_name == "task_store_trash":
            used_task_store = self.task_store_trash
        try:
            task = used_task_store.store_dict_id[task_id]
        except Exception as exc:
            # task_id is either None or it is not in store_dict_id
            util.dbgprint("exception in helper_get_task_or_default, semi-expected {}".format(str(exc)))
            self.error_msg_queue_list.append("Couldn't retrieve requested note.")
            return False, 0, 0, self.page_list_notes(no_history=True)
        return True, task_id, task, ""


    def page_edit_note(self):
        # TODO: docstring

        task_found, task_id, task, notfound_page = self.helper_get_task_or_default()
        if not task_found:
            self.error_msg_queue_list.append("Cannot edit specified note.")
            return notfound_page

        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        page_header_warning = None
        if self.error_msg_queue_note:
            page_header_warning = self.helper_convert_msg_queue_note_to_list_for_output()

        page_body = edit_note_page_template(self.task_store, task, self.sess_action_auth,
                                            editing_mode_existing_note=True, history_back_id=history_back_id,
                                            page_header_warning=page_header_warning)

        return page_body

    def page_add_new_note(self):
        # TODO: docstring

        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        task = Task()  # just a temporary one, won't even be saved; it's just so that the form below can stay unchanged

        page_body = edit_note_page_template(self.task_store, task, self.sess_action_auth,
                                            editing_mode_existing_note=False, history_back_id=history_back_id)

        return page_body

    def unauth_page_display_note_public(self, tainted_task_id, tainted_task_pubauthid):
        # TODO: docstring

        if tainted_task_id is None:
            raise Exception("task_id==None")

        if tainted_task_pubauthid is None:
            raise Exception("task_pubauthid==None")

        task = self.task_store.store_dict_id[tainted_task_id]
        if task is None:
            raise Exception("task==None")

        # too short strings are inherently insecure
        if len(task.public_share_auth) < 5:
            task.public_share_auth = util.create_id_task()
            raise Exception("task.public_share_auth insecure")

        # hashing&salting so that string comparison doesn't easily allow timing attacks
        if not util.safe_string_compare(task.public_share_auth, tainted_task_pubauthid):
            raise Exception("task_pubauthid=None")
        else:
            page_body = html_page_templates.unauth_page_display_note_public_template(
                tainted_task_id=tainted_task_id,
                tainted_task_pubauthid=tainted_task_pubauthid,
                task_store=self.task_store
            )

            return page_body

    def page_display_note(self):
        # TODO: docstring

        task_found, task_id, task, notfound_page = self.helper_get_task_or_default()
        if not task_found:
            self.error_msg_queue_list.append("Cannot display specified note.")
            return notfound_page

        alt_task_store_name = self.helper_get_alt_task_store_name()

        highlight_in_text = None
        try:
            highlight_in_text = [x for x in self.last_request_get_dict["highlight_in_text"]]  # not sanitized
            util.dbgprint(highlight_in_text)
        except Exception as exc:
            util.dbgprint("expected exception ama {}".format(str(exc)))

        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        page_header_list_of_warnings = None
        if self.error_msg_queue_note:
            page_header_list_of_warnings = self.helper_convert_msg_queue_note_to_list_for_output()

        page_body = html_page_templates.page_display_note_template(
            task_id=task.taskid,
            task=task,
            page_header_optional_list_of_warnings=page_header_list_of_warnings,
            alt_task_store_name=alt_task_store_name,
            highlight_in_text=highlight_in_text,
            history_back_id=history_back_id,
            self_sess_action_auth=self.sess_action_auth,
        )

        return page_body

    def page_list_notes(self, no_history=False):
        # TODO: docstring
        # main page - lists all notes

        list_taskid_desc = self.task_store.sort_taskid_list_descending_lamport()
        title = "woolnote - all notes"
        page_header_first_text = "all notes"

        if no_history:
            history_id = self.save_history([])
        else:
            history_id = self.save_history(["action"], alt_task_store_name=None)

        page_header_list_of_warnings = None
        page_header_small_text = None

        if self.error_msg_queue_list:
            page_header_list_of_warnings = self.helper_convert_msg_queue_list_to_list_for_output()
        else:
            try:
                # TODO: use asn library?
                # sha256_fp = read_pem_cert_fingerprint(SSL_CERT_PEM_PATH)
                page_header_small_text = config.SSL_CERT_PEM_FINGERPRINT
            except:
                page_header_small_text = "cannot get ssl cert sha256"

        return template_page_list_notes(list_taskid_desc=list_taskid_desc, title=title,
                                        history_back_id=history_id, primary_task_store=self.task_store,
                                        virtual_folders=self.woolnote_config.virtual_folders,
                                        page_header_first_text=page_header_first_text,
                                        page_header_optional_small_second_text=page_header_small_text,
                                        page_header_optional_list_of_warnings=page_header_list_of_warnings)

    def page_list_trash(self):
        # TODO: docstring

        list_taskid_desc = self.task_store_trash.sort_taskid_list_descending_lamport()
        title = "woolnote - trash"
        page_header_first_text = "notes in the trash"
        page_header_link_button_name = "reset filter"
        page_header_link_request_dict = {"action": "show_list"}
        page_header_list_of_warnings = None

        if self.error_msg_queue_list:
            page_header_list_of_warnings = self.helper_convert_msg_queue_list_to_list_for_output()

        history_id = self.save_history(["action"], alt_task_store_name=None)

        return template_page_list_notes(list_taskid_desc=list_taskid_desc, title=title,
                                        primary_task_store=self.task_store, alt_task_store=self.task_store_trash,
                                        alt_task_store_name="task_store_trash", history_back_id=history_id,
                                        virtual_folders=self.woolnote_config.virtual_folders,
                                        page_header_first_text=page_header_first_text,
                                        page_header_optional_link_button_name=page_header_link_button_name,
                                        page_header_optional_link_button_request_dict=page_header_link_request_dict,
                                        page_header_optional_list_of_warnings=page_header_list_of_warnings)

    def page_search_notes(self):
        # TODO: docstring

        task_store_name = "task_store"
        alt_task_store = None
        alt_task_store_name = self.helper_get_alt_task_store_name()
        if alt_task_store_name == "task_store_trash":
            task_store_name = alt_task_store_name
            alt_task_store = self.task_store_trash

        search_text = self.last_request_get_dict["search_text"][0].lower()
        list_taskid_desc, highlight_list = self.ui_backend.search_notes(task_store_name, search_text)

        # in the rest of the function, the variable should be None if it is the default task store
        if task_store_name == "task_store":
            task_store_name = None

        history_id = self.save_history(["search_text", "action"], alt_task_store_name=alt_task_store_name)

        title = "woolnote - search " + search_text

        page_header_first_text = "search " + search_text
        page_header_link_button_name = "reset filter"
        page_header_link_request_dict = {"action": "show_list"}
        page_header_list_of_warnings = None

        if self.error_msg_queue_list:
            page_header_list_of_warnings = self.helper_convert_msg_queue_list_to_list_for_output()

        return template_page_list_notes(list_taskid_desc=list_taskid_desc, title=title,
                                        highlight_in_notes=highlight_list, primary_task_store=self.task_store,
                                        alt_task_store=alt_task_store, alt_task_store_name=alt_task_store_name,
                                        history_back_id=history_id,
                                        virtual_folders=self.woolnote_config.virtual_folders,
                                        page_header_first_text=page_header_first_text,
                                        page_header_optional_link_button_name=page_header_link_button_name,
                                        page_header_optional_link_button_request_dict=page_header_link_request_dict,
                                        page_header_optional_list_of_warnings=page_header_list_of_warnings)

    def page_list_folder(self):
        # TODO: docstring


        alt_task_store_name = None
        alt_task_store = None
        try:
            alt_task_store_name = self.last_request_get_dict["alt_task_store_name"][0]
            if alt_task_store_name == "task_store_trash":
                alt_task_store = self.task_store_trash
            else:
                alt_task_store_name = None
                alt_task_store = None
        except Exception as exc:
            util.dbgprint("expected exception asa {}".format(str(exc)))
        used_task_store = self.task_store
        if alt_task_store:
            used_task_store = alt_task_store

        try:
            folder = self.last_request_get_dict["folder"][0]
            list_taskid_desc = used_task_store.filter_folder(folder)
        except Exception as exc:
            util.dbgprint("exception aoa, semi-expected {}".format(str(exc)))
            return self.page_list_notes(no_history=True)

        history_id = self.save_history(["folder", "action"], alt_task_store_name=alt_task_store_name)

        title = "woolnote - notes in " + folder

        page_header_first_text = "notes in " + folder
        page_header_link_button_name = "reset filter"
        page_header_link_request_dict = {"action": "show_list"}
        page_header_list_of_warnings = None

        if self.error_msg_queue_list:
            page_header_list_of_warnings = self.helper_convert_msg_queue_list_to_list_for_output()

        return template_page_list_notes(list_taskid_desc=list_taskid_desc, title=title,
                                        primary_task_store=self.task_store, alt_task_store=alt_task_store,
                                        alt_task_store_name=alt_task_store_name, history_back_id=history_id,
                                        virtual_folders=self.woolnote_config.virtual_folders,
                                        page_header_first_text=page_header_first_text,
                                        page_header_optional_link_button_name=page_header_link_button_name,
                                        page_header_optional_link_button_request_dict=page_header_link_request_dict,
                                        page_header_optional_list_of_warnings=page_header_list_of_warnings)

    def page_list_tag(self):
        # TODO: docstring


        alt_task_store_name = None
        alt_task_store = None
        try:
            alt_task_store_name = self.last_request_get_dict["alt_task_store_name"][0]
            if alt_task_store_name == "task_store_trash":
                alt_task_store = self.task_store_trash
            else:
                alt_task_store_name = None
                alt_task_store = None
        except Exception as exc:
            util.dbgprint("expected exception asa {}".format(str(exc)))
        used_task_store = self.task_store
        if alt_task_store:
            used_task_store = alt_task_store

        try:
            tag = self.last_request_get_dict["tag"][0]
            list_taskid_desc = used_task_store.filter_tag(tag)
        except Exception as exc:
            util.dbgprint("exception apa, semi-expected {}".format(str(exc)))
            return self.page_list_notes(no_history=True)

        history_id = self.save_history(["tag", "action"], alt_task_store_name=alt_task_store_name)

        title = "woolnote - notes in " + tag

        page_header_first_text = "notes in " + tag
        page_header_link_button_name = "reset filter"
        page_header_link_request_dict = {"action": "show_list"}
        page_header_list_of_warnings = None

        if self.error_msg_queue_list:
            page_header_list_of_warnings = self.helper_convert_msg_queue_list_to_list_for_output()

        return template_page_list_notes(list_taskid_desc=list_taskid_desc, title=title,
                                        primary_task_store=self.task_store, alt_task_store=alt_task_store,
                                        alt_task_store_name=alt_task_store_name, history_back_id=history_id,
                                        virtual_folders=self.woolnote_config.virtual_folders,
                                        page_header_first_text=page_header_first_text,
                                        page_header_optional_link_button_name=page_header_link_button_name,
                                        page_header_optional_link_button_request_dict=page_header_link_request_dict,
                                        page_header_optional_list_of_warnings=page_header_list_of_warnings)

    def page_note_list_multiple_select(self):
        # TODO: docstring

        tasks_to_delete = []
        try:
            list_taskid_desc_unfiltered = self.task_store.sort_taskid_list_descending_lamport()
            post_data_keys = list(self.last_request_post_data_dict.keys())
            for taskid in list_taskid_desc_unfiltered:
                task = self.task_store.store_dict_id[taskid]
                if taskid in post_data_keys:
                    tasks_to_delete.append(task)
        except Exception as exc:
            util.dbgprint("exception aqa, semi-expected {}".format(str(exc)))
            self.error_msg_queue_list.append("Cannot get the list of notes for multi-select manipulation.")
            return self.page_list_notes(no_history=True)

        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        page_body = html_page_templates.page_note_list_multiple_select_template(
            tasks_to_delete=tasks_to_delete,
            task_store=self.task_store,
            history_back_id=history_back_id,
            self_sess_action_auth=self.sess_action_auth
        )
        return page_body

    def page_delete_notes(self):
        # TODO: docstring

        if self.helper_sessactionauth_is_wrong():
            self.error_msg_queue_list.append("Cannot display note deletion page - wrong session?")
            return self.page_list_notes(no_history=True)

        tasks_to_delete = []
        try:
            delete_taskid_list = self.last_request_post_data_dict["taskid"]
            for taskid, task in self.task_store.store_dict_id.items():
                if taskid in delete_taskid_list:
                    tasks_to_delete.append(task)
        except:
            # util.dbgprint("delete_notes_page_page() - no post data detected")
            # get get data instead
            try:
                delete_taskid_list = self.last_request_get_dict["taskid"]
                for taskid, task in self.task_store.store_dict_id.items():
                    if taskid in delete_taskid_list:
                        tasks_to_delete.append(task)
            except Exception as exc:
                util.dbgprint("exception ara, semi-expected {}".format(str(exc)))
                self.error_msg_queue_list.append("Cannot display note deletion page - wrong request?")
                return self.page_list_notes(no_history=True)

        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        page_body = html_page_templates.page_delete_notes_template(
            tasks_to_delete=tasks_to_delete,
            history_back_id=history_back_id,
            self_sess_action_auth=self.sess_action_auth
        )

        return page_body

    def page_export_prompt(self):
        # TODO: docstring

        nonce = self.create_new_nonce()
        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        page_body = html_page_templates.page_export_prompt_template(
            nonce=nonce,
            history_back_id=history_back_id,
            self_sess_action_auth=self.sess_action_auth,
        )
        return page_body

    def page_import_prompt(self):
        # TODO: docstring

        nonce = self.create_new_nonce()
        history_back_id = self.helper_retrieve_last_request_get_dict_key_val_index_zero_or_return_none("history_back_id")

        page_body = html_page_templates.page_import_prompt_template(
            nonce=nonce,
            history_back_id=history_back_id,
            self_sess_action_auth=self.sess_action_auth,
        )
        return page_body

    def edit_folders_page(self):
        # TODO - shows a list of folders with links to edit them
        pass

    def edit_tags_page(self):
        # TODO - shows a list of tags with links to edit them
        pass

    def edit_folder_page(self):
        # TODO - shows a selected folder to edit and allows renaming or deleting
        pass

    def edit_tag_page(self):
        # TODO - shows a selected tag to edit and allows renaming or deleting
        pass
