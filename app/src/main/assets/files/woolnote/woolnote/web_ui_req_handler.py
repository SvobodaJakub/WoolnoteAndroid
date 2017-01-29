import urllib
from http.server import BaseHTTPRequestHandler
import sys
import traceback
import ssl

from woolnote import config
from woolnote import util
from woolnote import html_constants


# web interface request handler
###############################


def get_WebInterfaceHandlerLocal(woolnote_config, task_store, web_ui, ui_auth):
    # TODO: docstring
    class WebInterfaceHandlerLocal(BaseHTTPRequestHandler):
        # TODO: docstring

        # TODO
        # - login form
        # - public areas / public notes
        # - security tokens in get/post?

        HTTP_STATIC_RESOURCES = {
            "/uikit-2.27.1.gradient-customized.css": {
                "page_content": html_constants.CSS_UIKIT_2_27_1_STYLE_OFFLINE,
                "Content-Type": "text/css",
                "Cache-Control": "max-age=259200, public",
            },
            "/favicon.ico": {
                "page_content": "",
                "Content-Type": "text/html",
                "Cache-Control": "max-age=3600, public",
            },
        }

        def __init__(self, *args, **kwargs):
            # TODO: docstring
            self.last_request_get_dict = {}
            self.last_request_post_data_dict = {}
            self.last_request_post_data = ""
            self.last_request_path = ""
            self.headers = {}
            self.authenticated = False
            super().__init__(*args, **kwargs)

        def helper_check_permanent_pwd(self):
            # TODO
            pass
            try:
                full_path = self.path
                user_supplied_key, user_supplied_value = full_path.split("=")
                if not util.safe_string_compare(user_supplied_key.strip(), "/woolnote?woolauth"):
                    return False
                if 100 > len(user_supplied_value.strip()) > 6:
                    return ui_auth.check_permanent_pwd(user_supplied_value.strip())
                return False
            except:
                return False

        def helper_check_one_time_pwd(self):
            # TODO: docstring
            try:
                full_path = self.path
                user_supplied_key, user_supplied_value = full_path.split("=")
                if not util.safe_string_compare(user_supplied_key.strip(), "/woolnote?otp"):
                    return False
                if 100 > len(user_supplied_value.strip()) > 6:
                    return ui_auth.check_one_time_pwd(user_supplied_value.strip())
                return False
            except:
                return False

        def helper_get_request_authentication(self):
            # TODO: docstring
            """Determines whether the request is authenticated from path or from cookies."""

            self.authenticated = False

            # hashing&salting so that string comparison doesn't easily allow timing attacks
            # if self.path == ("/woolnote?woolauth=" + LOGIN_PASSWORD):
            # if util.safe_string_compare(self.path, "/woolnote?woolauth=" + config.LOGIN_PASSWORD):
            if self.helper_check_permanent_pwd():
                self.authenticated = True
                # will display page_content = web_ui.page_list_notes()
            if self.helper_check_one_time_pwd():
                self.authenticated = True
                # will display page_content = web_ui.page_list_notes()
            try:
                cookies = self.headers['Cookie'].split(";")
                for cookie in cookies:
                    keyval = cookie.split("=")
                    key = keyval[0].strip()
                    if key == "auth":
                        val = keyval[1].strip()
                        # hashing&salting so that string comparison doesn't easily allow timing attacks
                        # if val == ui_auth.return_cookie_authenticated():
                        if util.safe_string_compare(val, ui_auth.return_cookie_authenticated()):
                            self.authenticated = True
            except Exception as exc:
                util.dbgprint("exception in cookie handling {}".format(str(exc)))

        def get_request_data(self):
            # TODO: docstring
            """Retrieves and saves the request GET and POST data and determines whether the request is authenticated."""

            try:
                self.last_request_get_dict = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            except:
                self.last_request_get_dict = {}
            try:
                self.last_request_path = self.path
            except:
                self.last_request_path = ""
            try:
                self.last_request_post_data = self.rfile.read(int(self.headers['Content-Length'])).decode("utf-8")
            except:
                self.last_request_post_data = ""
            try:
                self.last_request_post_data_dict = urllib.parse.parse_qs(self.last_request_post_data)
            except:
                self.last_request_post_data_dict = {}

            self.authenticated = False
            self.helper_get_request_authentication()

        def req_handler_authenticated(self):
            # TODO: docstring
            page_content = "<html><body>N/A</body></html>"
            # reload the config settings (the config note could have been changed by the user)
            woolnote_config.read_from_config_note(task_store)

            def history_go_back():
                # TODO: docstring
                """Set the page to go back in history - either directly in page_content or using last_request_get_dict"""
                nonlocal page_content
                try:
                    util.dbgprint("history_back - try")
                    # history_back_id might not exist -> except
                    # history_back_id id might not exist in the history dict -> except
                    try:
                        history_id = self.last_request_get_dict["history_back_id"][0]
                    except:
                        util.dbgprint("history_back_id not found, using main_list")
                        history_id = "main_list"
                    if history_id == "main_list":
                        pass
                    else:
                        self.last_request_get_dict = web_ui.get_last_request_from_history_id(history_id)
                        web_ui.set_last_request(self.last_request_post_data_dict, self.last_request_get_dict)
                    util.dbgprint("history_back - end of try")
                except:
                    util.dbgprint("history_back - except")
                    pass

            def display_content_after_history_back_during_request_processing():
                # TODO: docstring
                """Display the right page after history_go_back() during processing of a request"""
                nonlocal page_content
                if "action" not in self.last_request_get_dict:
                    page_content = web_ui.page_list_notes(no_history=True)
                elif self.last_request_get_dict["action"][0] == "list_folder":
                    page_content = web_ui.page_list_folder()
                elif self.last_request_get_dict["action"][0] == "list_tag":
                    page_content = web_ui.page_list_tag()
                elif self.last_request_get_dict["action"][0] == "search_notes":
                    page_content = web_ui.page_search_notes()
                else:
                    page_content = web_ui.page_list_notes(no_history=True)

            # handle request to display a list from history (back/cancel buttons, not browser history)
            if "action" in self.last_request_get_dict:
                if self.last_request_get_dict["action"][0] == "history_back":
                    history_go_back()

            # copy the data about the current request into the web_ui so that it can act on them as well
            web_ui.set_last_request(self.last_request_post_data_dict, self.last_request_get_dict)

            try:
                if "action" not in self.last_request_get_dict:
                    page_content = web_ui.page_list_notes()

                elif self.last_request_get_dict["action"][0] == "display_note":
                    page_content = web_ui.page_display_note()
                elif self.last_request_get_dict["action"][0] == "dismiss_reminder_and_display_note":
                    web_ui.req_note_dismiss_reminder()
                    page_content = web_ui.page_display_note()

                elif self.last_request_get_dict["action"][0] == "req_display_otp":
                    web_ui.req_display_otp()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "list_folder":
                    page_content = web_ui.page_list_folder()

                elif self.last_request_get_dict["action"][0] == "list_tag":
                    page_content = web_ui.page_list_tag()

                elif self.last_request_get_dict["action"][0] == "search_notes":
                    page_content = web_ui.page_search_notes()

                elif self.last_request_get_dict["action"][0] == "list_trash":
                    page_content = web_ui.page_list_trash()

                elif self.last_request_get_dict["action"][0] == "edit_note":
                    page_content = web_ui.page_edit_note()

                elif self.last_request_get_dict["action"][0] == "add_new_note":
                    page_content = web_ui.page_add_new_note()

                elif self.last_request_get_dict["action"][0] == "delete_taskid":
                    page_content = web_ui.page_delete_notes()

                elif self.last_request_get_dict["action"][0] == "req_note_checkboxes_save":
                    web_ui.req_note_checkboxes_save()
                    page_content = web_ui.page_display_note()

                elif self.last_request_get_dict["action"][0] == "req_save_edited_note":
                    web_ui.req_save_edited_note()
                    page_content = web_ui.page_edit_note()

                elif self.last_request_get_dict["action"][0] == "req_save_new_note":
                    web_ui.req_save_new_note()
                    page_content = web_ui.page_edit_note()

                elif self.last_request_get_dict["action"][0] == "import_prompt":
                    page_content = web_ui.page_import_prompt()

                elif self.last_request_get_dict["action"][0] == "export_prompt":
                    page_content = web_ui.page_export_prompt()

                elif self.last_request_get_dict["action"][0] == "req_import_notes_permanent":
                    web_ui.req_import_notes_permanent()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "req_export_notes_permanent":
                    web_ui.req_export_notes_permanent()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "req_delete_taskid_permanent":
                    web_ui.req_delete_taskid_permanent()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "req_note_list_manipulate_foldermove":
                    web_ui.req_note_list_manipulate_foldermove()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "req_note_list_manipulate_tagadd":
                    web_ui.req_note_list_manipulate_tagadd()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "req_note_list_manipulate_tagdel":
                    web_ui.req_note_list_manipulate_tagdel()
                    history_go_back()
                    display_content_after_history_back_during_request_processing()

                elif self.last_request_get_dict["action"][0] == "note_list_multiple_select":
                    page_content = web_ui.page_note_list_multiple_select()

                else:
                    page_content = web_ui.page_list_notes()

            except Exception as exc:
                etype, evalue, etraceback = sys.exc_info()
                ss = util.sanitize_singleline_string_for_html
                cmps = util.convert_multiline_plain_string_into_safe_html
                page_content = """<html><body>Exception {exc}:<br/>
                    <pre>{tra}</pre><br/>
                    <a href="woolnote">list notes</a></body></html>""".format(exc=ss(repr(exc)), tra=cmps(
                    repr(traceback.format_exception(etype, evalue, etraceback))))
                page_content = page_content.replace("\\n", "<br>\n")
            return page_content

        def req_handler_unauthenticated(self):
            # TODO: docstring
            page_content = "<html><body>N/A</body></html>"
            try:
                if self.last_request_get_dict["action"][0] == "display_note":
                    task_id = self.last_request_get_dict["taskid"][0]
                    task_pubauthid = self.last_request_get_dict["pubauthid"][0]
                    page_content = web_ui.unauth_page_display_note_public(task_id, task_pubauthid)
            except:
                pass
            return page_content

        def helper_generate_page_contents(self):
            # TODO: docstring
            """Generates contents for the main woolnote functionality - the pages, request handlers, etc. Both authenticated and unauthenticated."""
            page_content = "<html><body>N/A</body></html>"
            if self.authenticated:
                page_content = self.req_handler_authenticated()
            else:
                # NOT authenticated!
                page_content = self.req_handler_unauthenticated()
            return page_content

        def req_handler(self):
            # TODO: docstring
            resource_found = False
            # handle static requests
            for resource in self.HTTP_STATIC_RESOURCES:
                if self.path.startswith(resource):
                    page_content = self.HTTP_STATIC_RESOURCES[resource]["page_content"]
                    resource_found = True
                    break
            # handle dynamic requests
            if not resource_found:
                page_content = self.helper_generate_page_contents()
            try:
                self.wfile.write(page_content.encode("utf-8"))
            except ssl.SSLEOFError:
                # TODO in woolnote.py - why is suppress_ragged_eofs ignored?
                util.dbgprint("ssl.SSLEOFError (#TODO in the code)")
            return

        def do_GET(self):
            # TODO: docstring
            self.get_request_data()
            self.do_HEAD()
            self.req_handler()
            return

        def do_POST(self):
            # TODO: docstring
            self.get_request_data()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            if self.authenticated:
                self.send_header("Set-cookie", "auth=" + ui_auth.return_cookie_authenticated())
            self.end_headers()
            self.req_handler()

        def do_HEAD(self):
            # TODO: docstring
            '''
            Handle a HEAD request.
            '''
            self.send_response(200)
            resource_found = False
            for resource in self.HTTP_STATIC_RESOURCES:
                if self.path.startswith(resource):
                    try:
                        content_type = self.HTTP_STATIC_RESOURCES[resource]["Content-Type"]
                        self.send_header("Content-Type", content_type)
                    except:
                        pass
                    try:
                        cache_control = self.HTTP_STATIC_RESOURCES[resource]["Cache-Control"]
                        self.send_header("Cache-Control", cache_control)
                    except:
                        pass
                    resource_found = True
                    break
            if not resource_found:
                self.send_header("Content-Type", "text/html")
            if self.authenticated:
                self.send_header("Set-cookie", "auth=" + ui_auth.return_cookie_authenticated())
            self.end_headers()

    return WebInterfaceHandlerLocal
