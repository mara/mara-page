"""Server-side syntax highlighting based on pygments"""

import pygments
import pygments.formatters
import pygments.lexers
from mara_page import _


def highlight(code: str, language: str):
    """
    Renders a code snipped into a syntax-highlighted html fragment
    Args:
        code: The code to render
        language: See "short names" in http://pygments.org/docs/lexers/
    """
    formatter = pygments.formatters.HtmlFormatter(nobackground=True, style='friendly')
    return [_.style[formatter.get_style_defs()],
            pygments.highlight(code, pygments.lexers.get_lexer_by_name(language, strip_all=True), formatter=formatter)]
