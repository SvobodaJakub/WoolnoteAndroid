# TODO docstring
# stuff in this file converts data to HTML
# It is there so that there is only one file in the entire project that generates HTML and thus only one file that has
# to be thoroughly checked for correct sanitization.

import urllib
import re
import os # TODO: sanitize all usages in this file - they render into HTML
from woolnote import util
from woolnote import html_constants
from woolnote import config
from woolnote.task_store import PLAIN, MARKUP
from collections import namedtuple


def create_tag_folder_js_selectors_html_fragment_list(element_name, tag_folder_list, adding=False):
    # TODO docstring
    # TODO: move to html_page_templates.py
    ss = util.sanitize_singleline_string_for_html
    tag_folder_list_html_fragment_list = []
    operator = "="
    append = ""
    if adding:
        operator = "+="
        append = ", "
    for tag_folder in tag_folder_list:
        tag_folder_list_html_fragment_list.append(""" | <a href="javascript:void(0);" onclick="javascript:document.getElementsByName('{ss_element_name}')[0].value{operator}'{ss_tag_folder}{append}';">{ss_tag_folder}</a>""".format(
            ss_element_name=ss(element_name),
            ss_tag_folder=ss(tag_folder),
            operator=operator,
            append=append
        ))
    return tag_folder_list_html_fragment_list



class FormattedLinkData():
    """
    Holds information from which an HTML link fragment can be created. Ensures proper html sanitization of the data.
    """
    def __init__(self):
        self.small = False
        self.red_bold = False
        self.request_params_dict = {}
        self.link_display_text = ""

    def to_html(self):
        # TODO docstring
        ss = util.sanitize_singleline_string_for_html
        request_params = urllib.parse.urlencode(self.request_params_dict)
        if self.small:
            small_open = "<small>"
            small_close = "</small>"
        else:
            small_open = ""
            small_close = ""
        if self.red_bold:
            span_open = """<span style="color: red; font-weight: bold;">"""
            span_close = "</span>"
        else:
            span_open = ""
            span_close = ""
        return """{small_open}<a href="/woolnote?{request_params}">{span_open}{ss_elem}{span_close}</a>{small_close}<br>""".format(
            request_params=request_params,
            ss_elem=ss(self.link_display_text),
            small_open=small_open,
            small_close=small_close,
            span_open=span_open,
            span_close=span_close
        )


class PageData():
    # TODO docstring
    BODY_TAG_ATTR_NONE = "BODY_TAG_ATTR_NONE"
    BODY_TAG_ATTR_JS_TEXTAREA_RESIZE = "BODY_TAG_ATTR_JS_TEXTAREA_RESIZE"

    def __init__(self):
        self.body_tag_attr_variant = self.BODY_TAG_ATTR_NONE
        super().__init__()

    def page_head_title_to_html(self):
        raise NotImplementedError()
        return title

    def page_header_to_html(self):
        raise NotImplementedError()
        return page_header

    def page_menu_to_html(self):
        raise NotImplementedError()
        return page_menu

    def page_main_content_to_html(self):
        raise NotImplementedError()
        return page_main_content

    def to_html(self):
        body_tag = "<body>"
        if self.body_tag_attr_variant == self.BODY_TAG_ATTR_JS_TEXTAREA_RESIZE:
            body_tag = "<body {} >".format(html_constants.HTML_ELEM_ATTR_JS_EVENTS_TEXTAREA_RESIZE)

        meta_lines = html_constants.HTML_VIEWPORT_META
        head_lines = html_constants.HTML_UIKIT_2_27_1_LINK_REL_LOCAL
        head_title_contents = self.page_head_title_to_html()

        jump_to_top_button = """<div id="jumptotopbutton" style="position: fixed; bottom: 15px; right: 10px; padding: 4px; border: 1px solid #ccc; background: #f6f6f6; color: #333; text-align: center; cursor: pointer; " onclick="scroll(0,0);"><div style="font-size: 16px;">&#x25B2;</div></div>"""  # jump to top button
        res_page_header_html = self.page_header_to_html()
        if res_page_header_html:
            page_header = "<div id=\"pageheader\">{}</div><br>".format(res_page_header_html)
        else:
            page_header = ""
        res_page_menu_html = self.page_menu_to_html()
        if res_page_menu_html:
            page_menu = "<div id=\"pagemenu\">{}</div><br>".format(res_page_menu_html)
        else:
            page_menu = ""
        res_page_main_content_html = self.page_main_content_to_html()
        if res_page_main_content_html:
            page_main_content = "<div id=\"pagemaincontent\">{}</div><br>".format(res_page_main_content_html)
        else:
            page_main_content = "<div id=\"pagemaincontent\">{}</div><br>".format(
                "Oops, some content should be here. An error occured, apparently.")

        body = """
        {jump_to_top_button}
        <div id="content" class="uk-margin-left uk-margin-right uk-margin-top uk-margin-bottom">
        {page_header}
        {page_menu}
        {page_main_content}
        </div>
        """.strip()

        body = body.format(
            jump_to_top_button=jump_to_top_button,
            page_header=page_header,
            page_menu=page_menu,
            page_main_content=page_main_content
        )

        dumb_template_html_page_main = """
            <html>
            <meta charset=utf-8>
            {meta_lines}
            <head>
            {head_lines}
            <title>{head_title_contents}</title>
            </head>
            {body_tag}
            {body_lines}
            </body>
            </html>""".strip()

        page = dumb_template_html_page_main.format(
            meta_lines=meta_lines,
            head_lines=head_lines,
            head_title_contents=head_title_contents,
            body_tag=body_tag,
            body_lines=body
        )

        return page

class PageEditBaseData(PageData):
    # TODO docstring
    def __init__(self):
        self.task_name = None
        self.folder_list = []
        self.tag_list = []
        self.task_tags = []
        self.task_folder = None
        self.task_body_format = MARKUP
        self.task_body = None
        self.task_public_share_auth = None
        self.task_taskid = None
        self.task_due_date = None
        self.sess_action_auth = None
        self.history_back_id = None
        self.page_header_warning = None
        self.body_tag_attr_variant = self.BODY_TAG_ATTR_JS_TEXTAREA_RESIZE
        super().__init__()

    def page_head_title_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        if self.task_name:
            title = "editing - " + ss(self.task_name)
        else:
            title = "editing - new woolnote note"
        return title

    def page_header_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        page_header = self.page_header_display_html_default
        if self.page_header_warning:
            page_header += " | " + ss(self.page_header_warning)
        return page_header

    def page_main_content_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        sme = util.sanitize_multiline_string_for_textarea_html

        folder_list_html_fragment_list = create_tag_folder_js_selectors_html_fragment_list("taskfolder", self.folder_list)
        tag_list_html_fragment_list = create_tag_folder_js_selectors_html_fragment_list("tasktags", self.tag_list, adding=True)

        tasktags = ", ".join(sorted(self.task_tags))

        text_formatting = self.task_body_format
        # used in HTML radio buttons
        checked_markup = ""
        checked_plaintext = ""
        if text_formatting == PLAIN:
            checked_plaintext = "checked"
        if text_formatting == MARKUP:
            checked_markup = "checked"

        try:
            pubauthid = self.task_public_share_auth
            # too short strings are inherently insecure (this validation is duplicate, the primary validation occurs on save and use)
            if len(pubauthid) < 5:
                pubauthid = util.create_id_task()
        except:
            # not a string
            pubauthid = util.create_id_task()

        request_params_puburl = urllib.parse.urlencode(
            {"action": "display_note", "taskid": self.task_taskid, "pubauthid": ss(self.task_public_share_auth)})

        task_html_fragment_list = []

        if self.display_header:
            task_html_fragment_list.append("""<div id="headerform" >""")
        else:
            task_html_fragment_list.append("""<div id="headerform" style="display: none; " >""")

        # sanitize and insert into HTML
        task_html_fragment_list.append("""
        <input type="text" name="taskname" style="width:95%;" value="{ss_task_name_}"><br>
        Due date: <input type="text" name="duedate" style="width:40%;" value="{ss_task_due_date_}"><br>
        Folder: <input type="text" name="taskfolder" style="width:40%;" value="{ss_task_folder_}"> {___join_folder_list_html_fragment_list_}<br>
        Tags: <input type="text" name="tasktags" style="width:80%;" value="{ss_tasktags_}, "><br> {___join_tag_list_html_fragment_list_}<br>
        Public share auth id: <input type="text" name="taskpubauthid" style="width:40%;" value="{ss_pubauthid_}"> <a href="/woolnote?{request_params_puburl}" >Public URL</a><br>
        Formatting: <input type="radio" name="formatting" value="markup" {checked_markup}> markup / <input type="radio" name="formatting" value="plaintext" {checked_plaintext}> plain text <br>
        </div >
        <input type="submit" class="uk-button uk-button-large uk-button-primary" value="Save">
        <input type="button" class="uk-button uk-button-large" value="show header"  onclick="{js_event_button}" ><br>
        <textarea name="taskbody" id="TaTb" style="width: 100%; height: 70%; margin: auto" {textarea_js_events} >{sme_task_body_}</textarea ><br>
        <input type="submit" class="uk-button uk-button-primary" value="Save">
        """.format(
            ss_task_name_=ss(self.task_name),
            ss_task_due_date_=ss(self.task_due_date),
            ss_task_folder_=ss(self.task_folder),
            ___join_folder_list_html_fragment_list_="".join(folder_list_html_fragment_list),
            ss_tasktags_=ss(tasktags),
            ___join_tag_list_html_fragment_list_="".join(tag_list_html_fragment_list),
            ss_pubauthid_=ss(pubauthid),
            request_params_puburl=request_params_puburl,
            sme_task_body_=sme(self.task_body),
            js_event_button="x = function() { var div = document.getElementById('headerform'); if (div.style.display !== 'none') { div.style.display = 'none'; } else { div.style.display = 'block'; } }; x(); ",
            textarea_js_events=html_constants.HTML_ELEM_ATTR_JS_EVENTS_TEXTAREA_RESIZE,
            checked_markup=checked_markup,
            checked_plaintext=checked_plaintext
        ).strip()
                                       )

        task_html_fragment_list.append(self.form_additional_values_html())

        request_params_save = self.request_params_save_to_html()


        page_main_content = """
         <form class="uk-form" action="/woolnote?{request_params_save}" method="post">
        {__n__join_task_html_fragment_list_}
        </form>
        """.format(
            request_params_save=request_params_save,
            __n__join_task_html_fragment_list_="\n".join(task_html_fragment_list)
        ).strip()

        return page_main_content

class PageEditNewData(PageEditBaseData):
    # TODO docstring
    def __init__(self):
        self.page_header_display_html_default = "create new note"
        self.display_header = True
        super().__init__()

    def request_params_save_to_html(self):
        request_params_save = urllib.parse.urlencode(
            {"action": "req_save_new_note", "sessactionauth": self.sess_action_auth,
             "history_back_id": self.history_back_id})
        return request_params_save

    def form_additional_values_html(self):
        return ""

    def page_menu_to_html(self):
        # requests and links for saving a new note
        request_params_list = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})

        page_menu = """
            <a href="/woolnote?{request_params_list}" class="uk-button">cancel editing</a>
            """.format(
            request_params_list=request_params_list,
        ).strip()

        return page_menu

class PageEditExistingData(PageEditBaseData):
    # TODO docstring
    def __init__(self):
        self.page_header_display_html_default = "edit note"
        self.display_header = False
        super().__init__()

    def request_params_save_to_html(self):
        request_params_save = urllib.parse.urlencode(
            {"action": "req_save_edited_note", "taskid": self.task_taskid, "sessactionauth": self.sess_action_auth,
             "history_back_id": self.history_back_id})
        return request_params_save

    def form_additional_values_html(self):
        # allow prevention of consuming requests missing POST data (page reload)
        return """<input type="hidden" name="post_action" value="req_save_edited_note">"""

    def page_menu_to_html(self):
        # requests and links for saving an existing edited note
        request_params_display = urllib.parse.urlencode(
            {"action": "display_note", "taskid": self.task_taskid, "history_back_id": self.history_back_id})
        request_params_list = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})

        page_menu = """
            <span {HTML_SPAN_STYLE_BIG} >
            <a href="/woolnote?{request_params_list}" class="uk-button uk-button-large">back to list</a>
            </span>
            <span {HTML_SPAN_STYLE_BIG} >
            <a href="/woolnote?{request_params_display}" class="uk-button uk-button-large">cancel editing</a>
            </span>
            """.format(
            HTML_SPAN_STYLE_BIG=html_constants.HTML_SPAN_STYLE_BIG,
            request_params_list=request_params_list,
            request_params_display=request_params_display
        ).strip()

        return page_menu


class PageListData(PageData):
    # TODO docstring
    TaskDetails = namedtuple("TaskDetails", ["task_taskid", "task_due_date", "task_name", "task_folder", "task_tags", "task_body" ])

    def __init__(self):
        self.page_title = None
        self.page_header_first_text = None
        self.page_header_optional_small_second_text = None
        self.page_header_optional_link_button_name = None
        self.page_header_optional_link_button_request_dict = None
        self.page_header_optional_list_of_warnings = None
        self.alt_task_store_name = None
        self.highlight_in_notes = None
        self.history_back_id = None

        # list of TaskDetails
        self.list_of_task_details = []

        # lists of FormattedLinkData
        self.folder_list = []
        self.tag_list = []
        self.virtfldr_list = []
        self.context_list = []
        self.overdue_reminder_list = []
        self.overdue_list = []
        self.reminder_list = []

        super().__init__()

    def page_head_title_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        if self.page_title:
            title = ss(self.page_title)
        else:
            title = "woolnote"
        return title

    def page_header_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        page_header = ""
        if self.page_header_first_text:
            page_header += ss(self.page_header_first_text)
        if self.page_header_optional_small_second_text:
            page_header += " | <small>{}</small>".format( ss(self.page_header_optional_small_second_text) )
        if self.page_header_optional_link_button_name and self.page_header_optional_link_button_request_dict:
            page_header += """ | <a href="/woolnote?{params}" class="uk-button">{button_name}</a>""".format(
                button_name=ss(self.page_header_optional_link_button_name),
                params=urllib.parse.urlencode(self.page_header_optional_link_button_request_dict),
            )
        if self.page_header_optional_list_of_warnings:
            page_header += " | <b>Warning: {}</b>".format(
                ss(" | ".join(self.page_header_optional_list_of_warnings))
            )
        return page_header

    def page_menu_to_html(self):
        return None

    def page_main_content_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        cmss = util.convert_multiline_string_into_safe_html_short_snippet
        sniplen = 100

        task_list_html_fragment_list = []
        for task in self.list_of_task_details:

            request_params_dict = {"action": "display_note", "taskid": task.task_taskid, "history_back_id": self.history_back_id}
            if self.highlight_in_notes is not None:
                request_params_dict.update({"highlight_in_text": self.highlight_in_notes})
            if self.alt_task_store_name is not None:
                request_params_dict.update({"alt_task_store_name": self.alt_task_store_name})

            # True so that a list of highlights is encoded as individual key=val1&key=val2&key=val3 etc.
            request_params = urllib.parse.urlencode(request_params_dict, True)
            due_date = task.task_due_date
            if due_date:
                due_date = " | " + due_date
            else:
                due_date = ""
            if self.alt_task_store_name != "task_store_trash":
                # there's no point in doing multi-selects in trash
                task_list_html_fragment_list.append("""<input type="checkbox" """ + "name=\"" + ss(task.task_taskid) + "\">")
            task_list_html_fragment_list.append(
                html_constants.HTML_NOTE_LINK_WITH_PREVIEW.format(
                    request_params=request_params,
                    sanitized_task_name=ss(task.task_name),
                    sanitized_due_date=ss(due_date),
                    sanitized_task_folder=ss(task.task_folder),
                    sanitized_task_tags=ss(", ".join(sorted(task.task_tags))),
                    sanitized_body_snippet=cmss(task.task_body, sniplen)
                )
            )

        folder_list_html_fragment = "\n".join( [ x.to_html() for x in self.folder_list ] )

        tag_list_html_fragment = "\n".join( [ x.to_html() for x in self.tag_list ] )

        virtfldr_list_html_fragment = "\n".join( [ x.to_html() for x in self.virtfldr_list ] )

        context_list_html_fragment = "\n".join( [ x.to_html() for x in self.context_list ] )

        if self.alt_task_store_name is None:
            # These are the red dismissable reminders - no point displaying them in trash and other alternative stores.
            overdue_reminders_list_html_fragment = "\n".join( [ x.to_html() for x in self.overdue_reminder_list ] )
        else:
            overdue_reminders_list_html_fragment = ""

        overdue_list_html_fragment = "\n".join( [ x.to_html() for x in self.overdue_list ] )

        reminders_list_html_fragment = "\n".join( [ x.to_html() for x in self.reminder_list ] )

        request_params_new_note = urllib.parse.urlencode({"action": "add_new_note", "history_back_id": self.history_back_id})
        request_params_note_list_multiple_select = urllib.parse.urlencode({"action": "note_list_multiple_select", "history_back_id": self.history_back_id})

        request_params_list_trash = urllib.parse.urlencode({"action": "list_trash", "history_back_id": self.history_back_id})
        request_params_import_prompt = urllib.parse.urlencode({"action": "import_prompt", "history_back_id": self.history_back_id})
        request_params_export_prompt = urllib.parse.urlencode({"action": "export_prompt", "history_back_id": self.history_back_id})
        request_params_req_display_otp = urllib.parse.urlencode({"action": "req_display_otp", "history_back_id": self.history_back_id})

        DIV_STYLE_REMINDERLIST = """ style="padding:1em 1em; clear: both;" """
        DIV_STYLE_TAGLIST = """ style="float: left; padding:1em 1em; " """
        DIV_STYLE_TAGLISTS = """ style="width: 100%; clear: left; " """
        DIV_STYLE_NOTELIST = """ style="width: 100%; clear: left; " """

        # TODO continue from here
        form_search_alt_task_store_name = ""
        if self.alt_task_store_name is not None:
            form_search_alt_task_store_name = """<input type="hidden" name="alt_task_store_name" value="{}">""".format(
                self.alt_task_store_name)
        # TODO: validate alt_task_store_name everywhere in *_to_html()?

        manipulate_selected_nodes = """<input type="submit" class="uk-button" value="Manipulate selected notes"><br>"""
        if self.alt_task_store_name == "task_store_trash":
            # there's no point in doing multi-selects in trash
            manipulate_selected_nodes = ""

        if overdue_reminders_list_html_fragment.strip():
            div_overdue_reminders = """
        <div {DIV_STYLE_REMINDERLIST} >
        overdue - new reminders (click to dismiss)
        <br>
        {__n__join_overdue_reminders_list_html_fragment_list_}
        <br>
        </div>

        """.format(
                DIV_STYLE_REMINDERLIST=DIV_STYLE_REMINDERLIST,
                __n__join_overdue_reminders_list_html_fragment_list_=overdue_reminders_list_html_fragment,
            )
        else:
            div_overdue_reminders = ""

        page_main_body = """
        <div {DIV_STYLE_TAGLISTS} >
        {div_overdue_reminders}
        <div {DIV_STYLE_TAGLIST} >
        folders
        <br>
        {__n__join_folder_list_html_fragment_list_}
        <br>
        </div>
        <div {DIV_STYLE_TAGLIST} >
        tags
        <br>
        {__n__join_tag_list_html_fragment_list_}
        <br>
        </div>
        <div {DIV_STYLE_TAGLIST} >
        contexts
        <br>
        {__n__join_context_list_html_fragment_list_}
        <br>
        </div>
        <div {DIV_STYLE_TAGLIST} >
        virtual folders
        <br>
        {__n__join_virtfldr_list_html_fragment_list_}
        <br>
        </div>
        <div {DIV_STYLE_TAGLIST} >
        overdue
        <br>
        {__n__join_overdue_list_html_fragment_list_}
        <br>
        </div>
        <div {DIV_STYLE_TAGLIST} >
        reminders
        <br>
        {__n__join_reminders_list_html_fragment_list_}
        <br>
        </div>
        <div {DIV_STYLE_TAGLIST} >
        other
        <br>
        <form class="uk-form" action="/woolnote" method="get">
        <input type="hidden" name="action" value="search_notes">
        <input type="hidden" name="history_back_id" value="{history_back_id}">
        {form_search_additional}
        <input type="text" name="search_text" >
        <input type="submit" class="uk-button" value="Search in notes"><br>
        </form>
        <br>
        <a href="/woolnote?{request_params_list_trash}">trash</a>
        <br>
        <a href="/woolnote?{request_params_import_prompt}">import</a>
        <br>
        <a href="/woolnote?{request_params_export_prompt}">export</a>
        <br>
        <a href="/woolnote?{request_params_req_display_otp}">display OTP</a>
        <br>
        </div>
        </div>

        <div {DIV_STYLE_NOTELIST}>
        <br>
        <span" ><a href="/woolnote?{request_params_new_note}" class="uk-button uk-button-large uk-button-primary">create a new note</a></span><br>

        <form class="uk-form" action="/woolnote?{request_params_note_list_multiple_select}" method="post">
        {manipulate_selected_nodes}
        <hr><br>

        {__n__join_task_list_html_fragment_list_}
        <br>
        </form>
        </div>
        """.format(
            DIV_STYLE_TAGLISTS=DIV_STYLE_TAGLISTS,
            DIV_STYLE_TAGLIST=DIV_STYLE_TAGLIST,
            __n__join_folder_list_html_fragment_list_=folder_list_html_fragment,
            __n__join_tag_list_html_fragment_list_=tag_list_html_fragment,
            __n__join_context_list_html_fragment_list_=context_list_html_fragment,
            __n__join_virtfldr_list_html_fragment_list_=virtfldr_list_html_fragment,
            __n__join_overdue_list_html_fragment_list_=overdue_list_html_fragment,
            div_overdue_reminders=div_overdue_reminders,
            __n__join_reminders_list_html_fragment_list_=reminders_list_html_fragment,
            DIV_STYLE_NOTELIST=DIV_STYLE_NOTELIST,
            request_params_new_note=request_params_new_note,
            request_params_note_list_multiple_select=request_params_note_list_multiple_select,
            manipulate_selected_nodes=manipulate_selected_nodes,
            __n__join_task_list_html_fragment_list_="\n".join(task_list_html_fragment_list),
            form_search_additional=form_search_alt_task_store_name,
            history_back_id=self.history_back_id,
            request_params_list_trash=request_params_list_trash,
            request_params_import_prompt=request_params_import_prompt,
            request_params_export_prompt=request_params_export_prompt,
            request_params_req_display_otp=request_params_req_display_otp
        )

        return page_main_body



class PageUnauthDisplayNoteData(PageData):
    # TODO docstring

    def __init__(self):
        self.task_name = None
        self.task_body = None

        super().__init__()

    def page_head_title_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        if self.task_name:
            title = ss(self.task_name) + " - woolnote"
        else:
            title = "woolnote"
        return title

    def page_header_to_html(self):
        return None

    def page_menu_to_html(self):
        return None

    def page_main_content_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        cms = util.convert_multiline_markup_string_into_safe_html
        mmcm = util.multiline_markup_checkbox_mapping

        task_html_fragment_list = []
        task_html_fragment_list.append("<hr><b>" + ss(self.task_name) + "</b><br>")
        task_html_fragment_list.append("<hr>" + mmcm(cms(self.task_body), self.task_body, disabled_checkboxes=True) + "<br>")

        page_main_body = """
            """ + "\n".join(task_html_fragment_list) + """
            """
        return page_main_body

class PageDisplayNoteData(PageData):
    # TODO docstring

    def __init__(self):
        self.task_text_formatting = None
        self.task_taskid = None
        self.task_due_date = None
        self.task_name = None
        self.task_folder = None
        self.task_tags = None
        self.task_body = None
        self.task_body_hash = None
        self.task_created_date = None
        self.task_changed_date = None
        self.task_id = None
        self.page_header_optional_list_of_warnings = None
        self.alt_task_store_name = None
        self.highlight_in_text = None
        self.history_back_id = None
        self.self_sess_action_auth = None

        super().__init__()

    def page_head_title_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        if self.task_name:
            title = ss(self.task_name) + " - woolnote"
        else:
            title = "woolnote"
        return title

    def page_header_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        page_header = ""
        if self.page_header_optional_list_of_warnings:
            page_header += " | <b>Warning: {}</b>".format(
                ss(" | ".join(self.page_header_optional_list_of_warnings))
            )
        return page_header

    def page_menu_to_html(self):
        request_params_list = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})
        page_menu = """
        <span """ + html_constants.HTML_SPAN_STYLE_BIG + """ " ><a href="/woolnote?""" + request_params_list + """" class="uk-button uk-button-large">back to list</a></span>
        """
        return page_menu

    def page_main_content_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        cmps = util.convert_multiline_plain_string_into_safe_html
        cms = util.convert_multiline_markup_string_into_safe_html
        mmcm = util.multiline_markup_checkbox_mapping

        highlight_in_text_sanitized = None
        if self.highlight_in_text:
            highlight_in_text_sanitized = [ss(x) for x in self.highlight_in_text]

        tasktags = ", ".join(sorted(self.task_tags))

        def highlight_string_in_html_text(text, highlight_list):
            if not highlight_list:
                return text

            def highlight(re_match):
                input_string = re_match.group(0)
                return "<span style='background-color: #FFFF00'>" + input_string + "</span>"

            part_re_highlight_match = "|".join([re.escape(x) for x in highlight_list])
            # case-insensitive (?i)
            highlighted = re.sub("(?i)" + part_re_highlight_match, highlight, text)
            return highlighted

        def hsiht(text):
            if highlight_in_text_sanitized:
                return highlight_string_in_html_text(text, highlight_in_text_sanitized)
            else:
                return text

        request_params_checkbox_save = urllib.parse.urlencode( {"action": "req_note_checkboxes_save", "taskid": self.task_taskid, "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id, "task_body_hash": self.task_body_hash})
        request_params_edit = urllib.parse.urlencode( {"action": "edit_note", "taskid": self.task_taskid, "history_back_id": self.history_back_id})
        request_params_delete = urllib.parse.urlencode( {"action": "delete_taskid", "taskid": self.task_taskid, "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id})
        task_html_fragment_list = []
        if self.alt_task_store_name is None:
            task_html_fragment_list.append("""<span style="font-size:20pt; " >""")
            task_html_fragment_list.append(
                """<a href="/woolnote?""" + request_params_edit + """" class="uk-button">""" + "edit note" + "</a>" + "<br>")
            task_html_fragment_list.append("""</span><br>""")
            task_html_fragment_list.append(
                """<a href="/woolnote?""" + request_params_delete + """" class="uk-button">""" + "delete note" + "</a>" + "<br>")
        task_html_fragment_list.append("<hr><b>" + ss(self.task_name) + "</b><br>")
        task_html_fragment_list.append("Folder: " + ss(self.task_folder) + "<br>")
        task_html_fragment_list.append("Tags: " + ss(tasktags) + "<br>")
        task_html_fragment_list.append("Due date: " + ss(self.task_due_date) + "<br>")
        task_html_fragment_list.append("Created: " + ss(self.task_created_date) + "<br>")
        task_html_fragment_list.append("Changed: " + ss(self.task_changed_date) + "<br>")
        if self.alt_task_store_name is None and self.task_text_formatting == MARKUP:
            task_html_fragment_list.append(
                """<form class="uk-form" action="/woolnote?""" + request_params_checkbox_save + """" method="post">""")
            task_html_fragment_list.append("""<input type="submit" class="uk-button" value="Save checkboxes"><br>""")
            task_html_fragment_list.append(
                """<input type="hidden" name="post_action" value="req_note_checkboxes_save">""")  # prevent consuming requests missing POST data (page reload)
            task_html_fragment_list.append("<hr>" + hsiht(mmcm(cms(self.task_body), self.task_body)) + "<br>")
            task_html_fragment_list.append("""</form>""")
        elif self.alt_task_store_name is None and self.task_text_formatting == PLAIN:
            task_html_fragment_list.append("<hr>" + hsiht(cmps(self.task_body)) + "<br>")
        else:
            task_html_fragment_list.append("<hr>" + hsiht(mmcm(cms(self.task_body), self.task_body)) + "<br>")
            task_html_fragment_list.append("""<br><hr>source: <hr><br>""")
            task_html_fragment_list.append(hsiht(cmps(self.task_body)) + """<br>""")

        page_main_body = """
        """ + "\n".join(task_html_fragment_list) + """
        """

        return page_main_body

class PageMultipleSelectData(PageData):
    # TODO docstring
    TaskDetails = namedtuple("TaskDetails", ["task_taskid", "task_due_date", "task_name", "task_folder", "task_tags", "task_body" ])

    def __init__(self):
        self.self_sess_action_auth = None
        self.history_back_id = None
        self.folder_list = []
        self.tag_list = []

        # list of TaskDetails
        self.task_details_to_delete = []

        super().__init__()

    def page_head_title_to_html(self):
        page_title = "woolnote - edit selected notes"
        return page_title

    def page_header_to_html(self):
        page_header = "edit selected notes"
        return page_header

    def page_menu_to_html(self):

        request_params_list_back = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})
        page_menu = """
        <span """ + html_constants.HTML_SPAN_STYLE_BIG + """ >
        <a href="/woolnote?""" + request_params_list_back + """" class="uk-button uk-button-large">cancel operation</a><br>
        </span>
        """
        return page_menu

    def page_main_content_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        cmss = util.convert_multiline_string_into_safe_html_short_snippet
        sniplen = 100

        manipulate_taskid_list_html_fragment_list = []
        for task_detail in self.task_details_to_delete:
            manipulate_taskid_list_html_fragment_list.append(
                """<input type="hidden" name="taskid" """ + "value=\"" + ss(task_detail.task_taskid) + "\">")

        folder_list_html_fragment_foldermove_list = create_tag_folder_js_selectors_html_fragment_list("foldermove", self.folder_list)
        tag_list_html_fragment_tagadd_list = create_tag_folder_js_selectors_html_fragment_list("tagadd", self.tag_list)
        tag_list_html_fragment_tagdel_list = create_tag_folder_js_selectors_html_fragment_list("tagdel", self.tag_list)

        request_params = urllib.parse.urlencode( {"action": "req_note_list_manipulate_foldermove", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id})
        foldermove_html_fragment = """
         <form class="uk-form" action="/woolnote?""" + request_params + """" method="post">
         Move to folder: <input type="text" name="foldermove" style="width:40%;" """ + " value=\"" + ss(
            config.DEFAULT_FOLDER) + "\"> " + "".join(folder_list_html_fragment_foldermove_list) + """
        """ + "\n".join(manipulate_taskid_list_html_fragment_list) + """
        <input type="submit" class="uk-button" value="Move to folder">
        <br>
        </form>
        """

        request_params = urllib.parse.urlencode( {"action": "req_note_list_manipulate_tagadd", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id})
        tagadd_html_fragment = """
         <form class="uk-form" action="/woolnote?""" + request_params + """" method="post">
         Add tag: <input type="text" name="tagadd" style="width:40%;" """ + " value=\"" + ss("") + "\"> " + "".join(
            tag_list_html_fragment_tagadd_list) + """
        """ + "\n".join(manipulate_taskid_list_html_fragment_list) + """
        <input type="submit" class="uk-button" value="Add tag">
        <br>
        </form>
        """

        request_params = urllib.parse.urlencode( {"action": "req_note_list_manipulate_tagdel", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id})
        tagdel_html_fragment = """
         <form class="uk-form" action="/woolnote?""" + request_params + """" method="post">
         Delete tag: <input type="text" name="tagdel" style="width:40%;" """ + " value=\"" + ss("") + "\"> " + "".join(
            tag_list_html_fragment_tagdel_list) + """
        """ + "\n".join(manipulate_taskid_list_html_fragment_list) + """
        <input type="submit" class="uk-button" value="Delete tag">
        <br>
        </form>
        """

        request_params = urllib.parse.urlencode({"action": "delete_taskid", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id})
        notedel_html_fragment = """
         <form class="uk-form" action="/woolnote?""" + request_params + """" method="post">
         Delete listed notes:
        """ + "\n".join(manipulate_taskid_list_html_fragment_list) + """
        <input type="submit" class="uk-button" value="Delete listed notes">
        <br>
        </form>
        """

        task_list_html_fragment_list = []
        for task in self.task_details_to_delete:
            taskid = task.task_taskid
            request_params = urllib.parse.urlencode({"action": "display_note", "taskid": taskid})
            task_list_html_fragment_list.append(html_constants.HTML_NOTE_LINK_WITH_PREVIEW.format(
                request_params=request_params,
                sanitized_task_name=ss(task.task_name),
                sanitized_due_date="",
                sanitized_task_folder=ss(task.task_folder),
                sanitized_task_tags=ss(", ".join(sorted(task.task_tags))),
                sanitized_body_snippet=cmss(task.task_body, sniplen)
            )
            )

        page_main_body = """
        """ + foldermove_html_fragment + """
        """ + tagadd_html_fragment + """
        """ + tagdel_html_fragment + """
        """ + notedel_html_fragment + """
        <br>
        <hr>
        <br>
        """ + "\n".join(task_list_html_fragment_list) + """
        """

        return page_main_body


class PageDeleteNotesData(PageData):
    # TODO docstring
    TaskDetails = namedtuple("TaskDetails", ["task_taskid", "task_due_date", "task_name", "task_folder", "task_tags", "task_body" ])

    def __init__(self):
        self.self_sess_action_auth = None
        self.history_back_id = None

        # list of TaskDetails
        self.task_details_to_delete = []

        super().__init__()

    def page_head_title_to_html(self):
        page_title = "woolnote - list of notes to delete"
        return page_title

    def page_header_to_html(self):
        page_header = "list of notes to delete"
        return page_header

    def page_menu_to_html(self):
        request_params_list = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})
        page_menu = """
        <span """ + html_constants.HTML_SPAN_STYLE_BIG + """ >
        <a href="/woolnote?""" + request_params_list + """" class="uk-button uk-button-large uk-button-primary">cancel operation</a><br>
        </span>
        """
        return page_menu

    def page_main_content_to_html(self):
        ss = util.sanitize_singleline_string_for_html
        cmss = util.convert_multiline_string_into_safe_html_short_snippet
        sniplen = 100

        task_list_html_fragment_list = []
        for task in self.task_details_to_delete:
            request_params = urllib.parse.urlencode({"action": "display_note", "taskid": task.task_taskid})
            task_list_html_fragment_list.append(html_constants.HTML_NOTE_LINK_WITH_PREVIEW.format(
                request_params=request_params,
                sanitized_task_name=ss(task.task_name),
                sanitized_due_date="",
                sanitized_task_folder=ss(task.task_folder),
                sanitized_task_tags=ss(", ".join(sorted(task.task_tags))),
                sanitized_body_snippet=cmss(task.task_body, sniplen)
            )
            )

        request_params_delete_permanent = urllib.parse.urlencode( {"action": "req_delete_taskid_permanent", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id})
        delete_taskid_list_html_fragment_list = []
        for task in self.task_details_to_delete:
            delete_taskid_list_html_fragment_list.append(
                """<input type="hidden" name="taskid" """ + "value=\"" + ss(task.task_taskid) + "\">")

        page_main_body = """
        """ + "\n".join(task_list_html_fragment_list) + """
        <br>
         <form class="uk-form" action="/woolnote?""" + request_params_delete_permanent + """" method="post">
        """ + "\n".join(delete_taskid_list_html_fragment_list) + """
          <input type="submit" class="uk-button uk-button-danger" value="Delete">
        </form>
        """

        return page_main_body




class PageExportPromptData(PageData):
    # TODO docstring

    def __init__(self):
        self.self_sess_action_auth = None
        self.history_back_id = None
        self.nonce = None

        super().__init__()

    def page_head_title_to_html(self):
        page_title = "woolnote - export notes"
        return page_title

    def page_header_to_html(self):
        page_header = "do you really want to export notes?"
        return page_header

    def page_menu_to_html(self):
        return None

    def page_main_content_to_html(self):

        if not self.nonce:
            raise Exception("nonce has not been set for the page template")

        request_params_list = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})
        request_params = urllib.parse.urlencode( {"action": "req_export_notes_permanent", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id, "nonceactionauth": self.nonce})

        page_main_body = """
        <span style="font-size:20pt; " >
        <a href="/woolnote?""" + request_params_list + """" class="uk-button">No - back to list</a><br>
        </span>
        <br>
        <br>
        <span style="font-size:20pt; " >
        <a href="/woolnote?""" + request_params + """" class="uk-button">Yes - export to """ + str(os.path.join(
            config.PATH_SAVE_DROPBOX_EXPORT, config.FILE_WOOLNOTE_ZIP)) + """</a><br>
        </span>
        """

        return page_main_body

class PageImportPromptData(PageData):
    # TODO docstring

    def __init__(self):
        self.self_sess_action_auth = None
        self.history_back_id = None
        self.nonce = None

        super().__init__()

    def page_head_title_to_html(self):
        page_title = "woolnote - import notes"
        return page_title

    def page_header_to_html(self):
        page_header = "do you really want to import notes?"
        return page_header

    def page_menu_to_html(self):
        return None

    def page_main_content_to_html(self):

        if not self.nonce:
            raise Exception("nonce has not been set for the page template")
        request_params_list = urllib.parse.urlencode({"action": "history_back", "history_back_id": self.history_back_id})
        request_params = urllib.parse.urlencode(
            {"action": "req_import_notes_permanent", "sessactionauth": self.self_sess_action_auth, "history_back_id": self.history_back_id, "nonceactionauth": self.nonce})
        request_params_replace = urllib.parse.urlencode(
            {"action": "req_import_notes_permanent", "sessactionauth": self.self_sess_action_auth, "replace_local": "yes", "history_back_id": self.history_back_id, "nonceactionauth": self.nonce})

        page_main_body = """
        <span style="font-size:20pt; " >
        <a href="/woolnote?""" + request_params_list + """" class="uk-button">No - back to list</a><br>
        </span>
        <br>
        Be careful - the "merge and import" functionality is experimental and you might experience data loss
        (and the potential need to manually restore notes from backups). The "replace all local notes" option is stable
        with the drawback that it causes Woolnote to forget the local state and loads all notes from the synchronization
        file (if you do this by mistake, you have to manually restore notes from backups).
        <br>
        <span style="font-size:20pt; " >
        <a href="/woolnote?""" + request_params + """" class="uk-button">Yes - merge and import from """ + str(os.path.join(
            config.PATH_LOAD_DROPBOX_IMPORT, config.FILE_WOOLNOTE_ZIP)) + """</a><br>
        </span>
        <br>
        <br>
        <span style="font-size:20pt; " >
        <a href="/woolnote?""" + request_params_replace + """" class="uk-button">Yes - replace all local notes with import from """ + str(os.path.join(
            config.PATH_LOAD_DROPBOX_IMPORT, config.FILE_WOOLNOTE_ZIP)) + """ (overwrite all notes!)</a><br>
        </span>
        """
        return page_main_body





