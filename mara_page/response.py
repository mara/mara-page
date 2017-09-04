"""A flask response class that adds titles, action buttons and assets"""

import typing

import flask

from mara_page import xml


class ActionButton:
    def __init__(self, action: str, label: str, title: str, icon: str):
        """
        A button that is displayed at the top of a page

        Args:
            action: An url or `javascript:foo()` function call
            label: The label of the button
            title: A help text
            icon: The icon of the button (from http://fontawesome.io/)
        """
        self.action = action
        self.title = title
        self.icon = icon
        self.label = label


class Response(flask.Response):
    def __init__(self,
                 html,
                 title: str,
                 action_buttons: typing.Optional[typing.List[ActionButton]] = None,
                 js_files: typing.Optional[typing.List[str]] = None,
                 css_files: typing.Optional[typing.List[str]] = None,
                 status_code: int = 200):
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
        self.status_code = status_code
        super().__init__(html)
