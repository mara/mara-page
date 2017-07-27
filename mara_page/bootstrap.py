"""Functions for creating bootstrap 4 compatible markup"""

from mara_page import _


def card(title_left='',
         title_right='',
         fixed_title_height: bool = False,
         body=[],
         sections=[],
         id_=None):
    """
    Renders a bootstrap card `bootstrap_card`_ 
    
    Args:
        title_left: A title that is displayed at the top left of the card
        title_right: A title that is displayed at the top right of the card
        fixed_title_height: When true, then the title is restricted to 1 line
        body: Elements to be shown on the card
        sections: Parts of the card that are separated by an horizontal line
        id_: Optional ID of the enclosing div.

    Returns:
        The rendered card
        
    .. _bootstrap_card:
       https://v4-alpha.getbootstrap.com/components/card/     
    """
    return _.div(class_="card", id_=id_)[
        _.div(class_='card-block')[
            (_.div(class_='card-title' + (' fixed-title-height' if fixed_title_height else ''))[
                 _.div(class_='card-title-left')[title_left],
                 _.div(class_='card-title-right')[title_right]]
             if title_left != '' or title_right != ''
             else ''),
            body],
        (_.ul(class_='list-group list-group-flush')[
             [_.li(class_='list-group-item')[section] for section in sections]]
         if sections
         else '')]


def table(headers: [str], rows: []):
    """
    Renders a bootstrap table with some defaults applied
     
    Args:
        headers: The column headers (list of strings)
        rows: All table rows (rendered trs)

    Returns:
        The rendered table
    """
    return _.div[
        _.table(class_="mara-table table table-hover table-condensed table-sm")[
            _.thead[_.tr[[_.th[header] for header in headers]]],
            _.tbody[rows]]]
