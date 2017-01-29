import os
import copy
import zipfile
from woolnote import config
from woolnote import util
from woolnote.task_store import Task, TaskStore


# UI backend
############

class UIBackend():
    # TODO: better docstring

    def __init__(self, task_store, task_store_trash):
        # TODO: docstring
        self.task_store = task_store
        self.task_store_trash = task_store_trash
        super().__init__()

    def save_new_note_permanent(self, task):
        # TODO: better docstring
        self.task_store.add(task)
        self.task_store.task_store_save()

    def save_edited_note_permanent(self, task):
        # TODO: better docstring
        task.changed_date = util.current_timestamp()
        self.task_store.touch(task.taskid)
        self.task_store.task_store_save()

    def import_notes_permanent(self, replace_local_request):
        """If replace_local_request == True, then the remote database simply replaces the local database. Returns error_message or None if no error."""
        # TODO: better docstring
        self.task_store.task_store_save()
        self.task_store_trash.task_store_save()

        util.tasks_backup(self.task_store, self.task_store_trash, s="imp0")

        # import the zip into the local directory so that it can be loaded
        with zipfile.ZipFile(os.path.join(config.PATH_LOAD_DROPBOX_IMPORT, config.FILE_WOOLNOTE_ZIP), "r") as importzip:
            importzip.extract(config.FILE_WOOLNOTE_DAT, config.PATH_SAVE_DB)  # overwrites

        use_task_store = self.task_store
        use_task_store_trash = self.task_store_trash
        use_task_remote_store = TaskStore(os.path.join(config.PATH_SAVE_DB, config.FILE_WOOLNOTE_DAT))
        use_task_remote_store.task_store_load()

        if replace_local_request:
            use_task_store.store_dict_id = {}
            use_task_store.task_store_load(alt_path=os.path.join(config.PATH_SAVE_DB, config.FILE_WOOLNOTE_DAT))
            use_task_store.update_lamport_clock(use_task_remote_store.export_lamport_clock)
            use_task_store.last_import_lamport_clock = use_task_store.lamport_clock
            return None

        if use_task_remote_store.last_import_lamport_clock < use_task_store.export_lamport_clock:
            # if the remote store is based on an older export than the last export of the local store, abort the operation
            # (bad stuff might happen when importing such files)
            error_message = "Cannot import - internal database export lamport clock = {}, external database last import lamport clock = {}. ".format(
                str(int(use_task_store.export_lamport_clock)),
                str(int(use_task_remote_store.last_import_lamport_clock)))
            return error_message

        use_task_store.update_lamport_clock(use_task_remote_store.export_lamport_clock)
        use_task_store.last_import_lamport_clock = use_task_store.lamport_clock

        def local_change(task_local):
            # util.dbgprint("def local_change(task_local):")
            # util.dbgprint(task_local.lamport_timestamp > task_local.export_lamport_timestamp)
            return task_local.lamport_timestamp > task_local.export_lamport_timestamp

        def remote_change(task_local, task_remote):
            # util.dbgprint("def remote_change(task_local, task_remote):")
            # util.dbgprint(task_local.export_lamport_timestamp < task_remote.lamport_timestamp)
            return task_local.export_lamport_timestamp < task_remote.lamport_timestamp

        def no_change(task_local, task_remote):
            # util.dbgprint("def no_change(task_local, task_remote):")
            # util.dbgprint(((local_change(task_local) == False) and (remote_change(task_local, task_remote) == False)))
            return ((local_change(task_local) == False) and (remote_change(task_local, task_remote) == False))

        def both_change(task_local, task_remote):
            # util.dbgprint("def both_change(task_local, task_remote):")
            # util.dbgprint((local_change(task_local) and remote_change(task_local, task_remote)))
            return (local_change(task_local) and remote_change(task_local, task_remote))
            # -> current local task
            #                       -> create new copy
            #                           -> changed taskid
            #                           -> changed name
            # -> current remote task overwrites the current local task

        def local_change_only(task_local, task_remote):
            # util.dbgprint("def local_change_only(task_local, task_remote):")
            # util.dbgprint((local_change(task_local) and not remote_change(task_local, task_remote)))
            return (local_change(task_local) and not remote_change(task_local, task_remote))
            # -> do nothing (will be exported to remote on next export)

        def remote_change_only(task_local, task_remote):
            # util.dbgprint("def remote_change_only(task_local, task_remote):")
            # util.dbgprint((remote_change(task_local, task_remote) and not local_change(task_local)))
            return (remote_change(task_local, task_remote) and not local_change(task_local))
            # -> import (overwrite local)

        def locally_trashed(task_remote):
            # util.dbgprint("def locally_trashed(task_remote):")
            # -> create temp copy
            #                       -> change taskid
            #                       -> change name
            #                       -> save into local trash
            # util.dbgprint (task_remote.taskid in use_task_store_trash.store_dict_id)
            return task_remote.taskid in use_task_store_trash.store_dict_id

        def remotely_trashed(task_local):
            # util.dbgprint("def remotely_trashed(task_local):")
            in_local_not_remote = task_local.taskid not in use_task_remote_store.store_dict_id
            in_remote_known_then_trashed = task_local.export_lamport_timestamp == use_task_store.export_lamport_clock
            # util.dbgprint((in_local_not_remote and in_remote_known_then_trashed))
            return (in_local_not_remote and in_remote_known_then_trashed)
            # -> trash the local copy

        def new_in_local(task_local):
            # util.dbgprint("def new_in_local(task_local):")
            in_local_not_remote = task_local.taskid not in use_task_remote_store.store_dict_id
            in_remote_known_then_trashed = task_local.export_lamport_timestamp == use_task_store.export_lamport_clock
            # util.dbgprint((in_local_not_remote and not in_remote_known_then_trashed))
            return (in_local_not_remote and not in_remote_known_then_trashed)
            # -> do nothing (will be exported to remote on next export)

        def new_in_remote(task_remote):
            # util.dbgprint("def new_in_remote(task_remote):")
            # util.dbgprint((task_remote.taskid not in use_task_store_trash.store_dict_id) and (task_remote.taskid not in use_task_store.store_dict_id))
            return ((task_remote.taskid not in use_task_store_trash.store_dict_id) and (
                task_remote.taskid not in use_task_store.store_dict_id))
            # -> import

        # util.dbgprint("set_tasks_local")
        set_tasks_local = set(use_task_store.store_dict_id.keys())
        # util.dbgprint(str(repr(set_tasks_local)))
        set_tasks_local_processed = set()
        # util.dbgprint("set_tasks_remote")
        set_tasks_remote = set(use_task_remote_store.store_dict_id.keys())
        # util.dbgprint(str(repr(set_tasks_remote)))
        set_tasks_remote_processed = set()

        # go through remote tasks, sync them, mark both sides as processed
        for taskid in set_tasks_remote:
            task_remote = use_task_remote_store.store_dict_id[taskid]
            # util.dbgprint("task_remote.taskid=" + task_remote.taskid + ", name=" + task_remote.name)
            if taskid in set_tasks_local:
                task_local = use_task_store.store_dict_id[taskid]
                # util.dbgprint("task_local.taskid=" + task_local.taskid + ", name=" + task_local.name)
                if remote_change_only(task_local, task_remote):
                    use_task_store.add_deserialized(task_remote)  # import (overwrite local)
                if local_change_only(task_local, task_remote):
                    pass
                if both_change(task_local, task_remote):
                    # -> current local task
                    #                       -> create new copy
                    #                           -> changed taskid
                    #                           -> changed name
                    # -> current remote task overwrites the current local task
                    tmp_task = copy.copy(task_local)
                    tmp_task.name += " (conflicted local copy, conflict date " + util.current_timestamp() + ", orig ID " + tmp_task.taskid + ")"
                    tmp_task.taskid = util.create_id_task()
                    use_task_store.add(tmp_task)
                    use_task_store.add_deserialized(task_remote)
                set_tasks_local_processed.add(task_local.taskid)
                set_tasks_remote_processed.add(task_remote.taskid)

        # go through unprocessed remote tasks, sync them, mark as processed
        for taskid in set_tasks_remote:
            if taskid not in set_tasks_remote_processed:
                task_remote = use_task_remote_store.store_dict_id[taskid]
                # util.dbgprint("task_remote.taskid=" + task_remote.taskid + ", name=" + task_remote.name)
                if locally_trashed(task_remote):
                    # -> create temp copy
                    #                       -> change taskid
                    #                       -> change name
                    #                       -> save into local trash
                    tmp_task = copy.copy(task_remote)
                    tmp_task.name += " (remote backup of locally trashed mote, backup date " + util.current_timestamp() + ", orig ID " + tmp_task.taskid + ")"
                    tmp_task.taskid = util.create_id_task()
                    use_task_store_trash.add(tmp_task)

                if new_in_remote(task_remote):
                    # -> import
                    use_task_store.add_deserialized(task_remote)  # import
            set_tasks_remote_processed.add(task_remote.taskid)

        # go through unprocessed local tasks, sync them, mark as processed
        for taskid in set_tasks_local:
            if taskid not in set_tasks_local_processed:
                task_local = use_task_store.store_dict_id[taskid]
                # util.dbgprint("task_local.taskid=" + task_local.taskid + ", name=" + task_local.name)
                if remotely_trashed(task_local):
                    # -> trash the local copy
                    use_task_store_trash.add_deserialized(task_local)
                    use_task_store.remove(task_local.taskid)
                    pass
                if new_in_local(task_local):
                    # -> do nothing (will be exported to remote on next export)
                    pass
            set_tasks_local_processed.add(task_local.taskid)

        util.tasks_backup(self.task_store, self.task_store_trash, s="imp1")
        return None

    def export_notes_permanent(self):
        """
        Has a permanent effect - calls task_store.task_store_save(), exports database
        """
        # TODO: better docstring

        util.tasks_backup(self.task_store, self.task_store_trash)

        # set clock
        self.task_store.export_lamport_clock = self.task_store.lamport_clock
        for taskid, task in self.task_store.store_dict_id.items():
            task.export_lamport_timestamp = self.task_store.export_lamport_clock

        # save the main database
        self.task_store.task_store_save()
        self.task_store_trash.task_store_save()

        # export to .dat file (without ZIP, so to the same path as the main database)
        self.task_store.task_store_save(alt_path=os.path.join(config.PATH_SAVE_DB, config.FILE_WOOLNOTE_DAT))

        # export the .dat to .zip
        with zipfile.ZipFile(os.path.join(config.PATH_SAVE_DROPBOX_EXPORT, config.FILE_WOOLNOTE_ZIP), "w",
                             compression=zipfile.ZIP_DEFLATED) as exportzip:
            exportzip.write(os.path.join(config.PATH_SAVE_DB, config.FILE_WOOLNOTE_DAT), arcname=config.FILE_WOOLNOTE_DAT,
                            compress_type=zipfile.ZIP_DEFLATED)

    def delete_taskid_permanent(self, task_id_list):
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        # TODO: better docstring
        for taskid in task_id_list:
            task = self.task_store.store_dict_id[taskid]
            self.task_store_trash.add(task)
            self.task_store.remove(taskid)
        self.task_store.task_store_save()
        self.task_store_trash.task_store_save()

    def notes_tagdel_permanent(self, task_id_list, tagdel):
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        # TODO: better docstring
        for taskid in task_id_list:
            task = self.task_store.store_dict_id[taskid]
            if tagdel in task.tags:
                self.task_store.touch(task.taskid)
                task.tags.discard(tagdel)
        self.task_store.task_store_save()

    def notes_tagadd_permanent(self, task_id_list, tagadd):
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        # TODO: better docstring
        for taskid in task_id_list:
            task = self.task_store.store_dict_id[taskid]
            self.task_store.touch(task.taskid)
            task.tags.add(tagadd)
        self.task_store.task_store_save()

    def notes_foldermove_permanent(self, task_id_list, foldermove):
        """
        Has a permanent effect - calls task_store.task_store_save()
        """
        # TODO: better docstring
        for taskid in task_id_list:
            task = self.task_store.store_dict_id[taskid]
            self.task_store.touch(task.taskid)
            task.folder = foldermove
        self.task_store.task_store_save()

    def search_notes(self, task_store_name, search_query):
        """
        Returns a list of tasks from the specified task store that match the search query and a list of strings to highlight (matches).
        """
        # TODO: better docstring
        if task_store_name == "task_store":
            used_task_store = self.task_store
        elif task_store_name == "task_store_trash":
            used_task_store = self.task_store_trash
        elif task_store_name == None:
            used_task_store = self.task_store
        else:
            raise ValueError("Unknown task store name - {}".format(task_store_name))

        list_taskid_desc_unfiltered = used_task_store.sort_taskid_list_descending_lamport()
        list_taskid_desc = []

        tokens = util.search_expression_tokenizer(search_query)
        tree_root = util.search_expression_build_ast(tokens)
        highlight_list = []
        list_taskid_desc = util.search_expression_execute_ast_node(tree_root, used_task_store,
                                                                   fulltext_search_strings=highlight_list)

        return list_taskid_desc, highlight_list
