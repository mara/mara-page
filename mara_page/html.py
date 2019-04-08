"""Various html generating utility functions"""

import uuid

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
    import pygments.formatters
    import pygments.lexers

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


def spinner_js_function() -> [str]:
    """Creates a javascript function that returns the markup of `spinner` """
    return _.script["function spinner() { return '" + str(spinner()) + "' };"]


def asynchronous_content(url: str, div_id: str = None) -> [str]:
    """
    Creates a div whose content will be asynchronously replaced with the content retrieved from `url`.

    Requires the implementation of the javascript function `loadContentAsynchronously` that takes four arguments
    - the container div
    - the url to load
    - a localStorage key for storing the final height of the div
    - an optional javascript snippet that is called once the content is loaded

    Args:
        url: The url from which to retrieve the content
        div_id: The id of the container div

    Returns:
        Html markup of the container div
    """
    div_id = div_id or str(uuid.uuid1())
    return _.div(id=div_id)[
        spinner(),
        _.script["""
 
(function() {
    // immediately (even before the DOM is completely loaded) set the height of the div 
    // to the last content height (stored in local storage) to avoid height flickering  
    var divHeightKey = 'div-height--' + window.location.pathname + '--' + '""" + url + """';
    var divHeight = localStorage.getItem(divHeightKey);
    if (divHeight) {
        document.getElementById('""" + div_id + """').style.height = divHeight + 'px';    
    }
    
    document.addEventListener('DOMContentLoaded', function() {
        if (typeof loadContentAsynchronously == 'undefined') {
            console.error('Please implement function "loadContentAsynchronously"');
        } else {
            loadContentAsynchronously('""" + div_id + """', '""" + url + """', divHeightKey);
        }
    });
})();
"""]]
