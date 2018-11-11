"""A flask response class that adds titles, action buttons and assets"""

import typing

import flask


from mara_page.bootstrap import ActionButton

class Response(flask.Response):
    def __init__(self,
                 html,
                 title: str,
                 action_buttons: typing.Optional[typing.List[ActionButton]] = None,
                 js_files: typing.Optional[typing.List[str]] = None,
                 css_files: typing.Optional[typing.List[str]] = None,
                 status: int = 200):
        """
        A rich html response with additional information for applying a page layout

        Args:
            html: The content of the page
            title: The title to be displayed in the page header
            action_buttons: Global actions for the page
            js_files: URL paths of js files to include
            css_files: URL paths of css files to include
            status_code: The http status code
        """
        self.title = title
        self.action_buttons = action_buttons or []
        self.js_files = js_files or []
        self.css_files = css_files or []
        super().__init__(html, status)
