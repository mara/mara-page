"""Functions for creating bootstrap 4 compatible markup"""

from mara_page import _


def card(header_left='', header_right='', fixed_header_height: bool = False, body=[], sections=[]):
    """
    Renders a bootstrap card `bootstrap_card`_ 
    
    Args:
        header_left: A header that is displayed at the top left of the card
        header_right: A header that is displayed at the top right of the card
        fixed_header_height: When true, then the header is restricted to 1 line
        body: Elements to be shown on the card
        sections: Parts of the card that are separated by an horizontal line

    Returns:
        The rendered card
        
    .. _bootstrap_card:
       https://v4-alpha.getbootstrap.com/components/card/     
    """
    return _.div(class_="card")[
        (_.div(class_='card-header' + (' fixed-header-height' if fixed_header_height else ''))[
             (_.div(class_='card-header-left')[header_left] if header_left else ''),
             (_.div(class_='card-header-right')[header_right] if header_right else '')]
         if header_left != '' or header_right != ''
         else ''),

        (_.div(class_='card-block')[_.div(class_='overflow-wrapper')[body]] if body else ''),
        [[_.hr(style='width:100%; margin:0px;'),
          _.div(class_='card-block')[_.div(class_='overflow-wrapper')[section]]] for section in sections] or ''
    ]


def table(headers: [str], rows: []):
    """
    Renders a bootstrap table with some defaults applied
     
    Args:
        headers: The column headers (list of strings)
        rows: All table rows (rendered trs)

    Returns:
        The rendered table
    """
    return _.table(class_='mara-table table table-condensed table-sm')[
            _.thead[_.tr[[_.th[header] for header in headers]]],
            _.tbody[rows]]
