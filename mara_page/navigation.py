"""Definition of navigation entries"""

import typing


class NavigationEntry:
    def __init__(self,
                 label: str,
                 uri_fn: typing.Callable = lambda: '#',
                 icon: str = None,
                 rank: int = 1,
                 description: str = None,
                 visible: bool = True,
                 children: typing.Optional[typing.List['NavigationEntry']] = None):
        """
        A single entry of the navigation sidebar.

        Args:
            label: The text that is displayed on the entry
            uri: A function that returns the uri of the linked page (not used when entry has children)
                 This needs to a callable because the app context for url creation is not known yet
            icon: An optional icon of the link (from http://fontawesome.io/)
            rank: How to sort entries within siblings
            description: An optional help text
            visible: When False, then the entry is not shown
            children: A list of sub-entries
        """
        self.label = label
        self.uri_fn = uri_fn
        self.icon = icon
        self.rank = rank
        self.description = description
        self.children = []
        self.parent = None
        self.visible = visible
        if children:
            for child in children:
                self.add_child(child)

    def add_child(self, child: 'NavigationEntry'):
        self.children.append(child)
        child.set_parent(self)

    def set_parent(self, parent: 'NavigationEntry'):
        """Sets the parent of the entry"""
        self.parent = parent

    def __repr__(self):
        return '<NavigationEntry "' + self.label + '">'

    def __hash__(self) -> int:
        return hash((self.label, self.icon, self.description))

    def __eq__(self, o: 'NavigationEntry') -> bool:
        return self.label == o.label and self.icon == o.icon and self.description == o.description

