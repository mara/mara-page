"""Functions for creating bootstrap 4 compatible markup"""

import uuid

from mara_page import _

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


def card(header_left='', header_right='', fixed_header_height: bool = True,
         body=[], sections=[], id: str = None, action_buttons: [str] = None):
    """
    Renders a bootstrap card `bootstrap_card`_ 
    
    Args:
        header_left: A header that is displayed at the top left of the card
        header_right: A header that is displayed at the top right of the card
        fixed_header_height: When true, then the header is restricted to 1 line
        body: Elements to be shown on the card
        sections: Parts of the card that are separated by an horizontal line
        id: An optional id for the outer dom element of the card
    Returns:
        The rendered card
        
    .. _bootstrap_card:
       https://v4-alpha.getbootstrap.com/components/card/     
    """
    return _.div(id=id or uuid.uuid1(), class_="card mara-card")[
        (_.div(class_='card-header' + (' fixed-header-height' if fixed_header_height else ''))[
             (_.div(class_='card-header-left')[header_left] if header_left else ''),
             (_.div(class_='card-header-right')[header_right] if header_right else '')]
         if header_left != '' or header_right != ''
         else ''),

        (_.div(class_='card-block')[_.div(class_='card-block-content')[body]] if body else ''),
        [_.div(class_='card-block card-section')[_.div(class_='card-block-content')[section]]
         for section in sections] or ''
    ]


def table(headers: [str], rows: [], id: str = None):
    """
    Renders a bootstrap table with some defaults applied
     
    Args:
        headers: The column headers (list of strings)
        rows: All table rows (rendered trs)
        id: An optional id for the table
    Returns:
        The rendered table
    """
    return _.table(class_='mara-table table table-hover table-condensed table-sm'
                          + (' mara-table-float-header' if headers else ''),
                   id=id or uuid.uuid1())[
        _.thead[_.tr[[_.th[header] for header in headers]]],
        _.tbody[rows]]


def button(url: str, label: str, title: str, icon: str, id: str = None):
    """
    Renders a bootstrap button
    Args:
        url: The action to perform
        label: The button label
        title: A help message
        icon: An icon from the `fontawesome`_ collection
        id: An id that is added to the element
    Returns:
        The rendered button

    .. _fontawesome:
       http://fontawesome.io/icons/
    """
    return _.a(class_='btn mara-button', href=url, title=title, id=id or uuid.uuid1())[
        _.span(class_='fa fa-' + icon)[''], ' ', label]
