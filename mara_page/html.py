"""Various html generating utility functions"""

import uuid
import json
import pygments
import pygments.formatters
import pygments.lexers
from mara_page import _


def highlight_syntax(code: str, language: str) -> [str]:
    """
    Renders a code snipped into a syntax-highlighted html fragment

    Args:
        code: The code to render
        language: See "short names" in http://pygments.org/docs/lexers/
    Returns:
        html markup
    """
    formatter = pygments.formatters.HtmlFormatter(nobackground=True, style='friendly')
    return [_.style[formatter.get_style_defs()],
            pygments.highlight(code, pygments.lexers.get_lexer_by_name(language, strip_all=True), formatter=formatter)]


def spinner() -> [str]:
    """
    Returns markup for an animated load spinner.

    The default version requires font-awesome to be installed

    Returns: html markup
    """
    return _.span(class_='fa fa-spinner fa-spin')[' ']


def asynchronous_content(url: str, on_success_js:str = None) -> [str]:
    """
    Creates a div whose content will be asynchronously replaced with the content retrieved from `url`.

    Requires the implementation of the javascript function `loadContentAsynchronously` that takes four arguments
    - the container div
    - the url to load
    - a localStorage key for storing the final height of the div
    - an optional javascript snippet that is called once the content is loaded

    Args:
        url: The url from which to retrieve the content
        on_success_js: A javascript snippet that is executed when the ajax call succeeds

    Returns:
        Html markup of the container div
    """
    id = str(uuid.uuid1())
    return _.div(id=id)[
        spinner(),
        _.script["""
// set the height of the div to last content height (stored in local storage) 
(function() {
    var divHeightKey = 'div-height--' + window.location.pathname + '--' + '""" + url + """';
    var divHeight = localStorage.getItem(divHeightKey);
    if (divHeight) {
        document.getElementById('""" + id + """').style.height = divHeight + 'px';    
    }
    
    document.addEventListener('DOMContentLoaded', function() {
        if (typeof loadContentAsynchronously == 'undefined') {
            console.error('Please implement function "loadContentAsynchronously"');
        } else {
            loadContentAsynchronously('""" + id + """', '"""
                     + url + """', divHeightKey, """ + (json.dumps(on_success_js) if on_success_js else '') + """);
        }
    });
})();
"""]]
