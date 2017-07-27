"""Expressing Html / XML document fragments in pure python syntax.

Examples:
    >>> print(_.div)
    <div/>

    >>> print(_.div['Hello world!'])
    <div>Hello world!</div>

    >>> print(_.div(style='color:red')['Hello world!'])
    <div style="color:red">Hello world!</div>

    >>> print(_.div(style='color:red', _class='foo')['Hello ', _.span(style='color:green')['world'], '!'])
    <div style="color:red" class="foo">Hello <span style="color:green">world</span>!</div>

    >>> print(_.ul[[_.li['item ', str(i)] for i in [1, 2, 3]]])
    <ul><li>item 1</li><li>item 2</li><li>item 3</li></ul>


It is very much inspired by `CL-WHO`_ for Common Lisp and `Hiccup`_ for Clojure.

For Python, there is also
 - `pyhiccup`_ (unfortunately GPL3 licenced)
 - `stan`_ (part of a web framework that is too big to have as a dependency)
 - `lmxl builder`_ (hidden in a huge XML library)

.. _CL-WHO:
   http://weitz.de/cl-who/

   _Hiccup:
   https://github.com/weavejester/hiccup

   _pyhiccup:
   https://pypi.python.org/pypi/pyhiccup

   _stan:
   https://github.com/twisted/nevow/blob/master/nevow/stan.py

   _lxml builder:
   http://lxml.de/api/lxml.html.builder-module.html

"""


class XMLElement():
    """Representation of a html / xml element with attributes and children"""

    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.attributes = {}
        self.children = []

    def __call__(self, **kwargs):
        """
        Adds attributes to the element. When the desired attribute name is a reserved
        python keyword, then postfix it with '_'
        """
        for attribute_name, value in kwargs.items():
            if attribute_name[0] == '_':
                import warnings
                warnings.warn('Prefixing python keywords is deprecated, please postfix such names', FutureWarning, stacklevel=2)
                attribute_name = attribute_name[1:]
            if attribute_name[-1] == '_':
                attribute_name = attribute_name[:-1]
            self.attributes[attribute_name] = str(value)
        return self

    def __getitem__(self, *children):
        """Adds children to the element"""
        self.children = XMLElement.flatten(children)
        return self

    def __str__(self):
        """Renders the element and it's children"""
        result = ['<', str(self.tag_name)]
        if self.attributes:
            for a in self.attributes:
                result.extend([' ', a, '="' + self.attributes[a], '"'])
        if self.children:
            result.extend('>')
            for child in self.children:
                result.extend(str(child))
            result.extend(['</', self.tag_name, '>'])
        else:
            result.extend('/>')

        return ''.join(result)

    @classmethod
    def flatten(cls, list):
        out = []
        for item in list:
            if isinstance(item, (str, XMLElement)):
                out.append(item)
            elif hasattr(item, '__iter__'):
                out.extend(XMLElement.flatten(item))
            else:
                raise TypeError('"{}" is not a str'.format(repr(item)))
        return out


class XMLElementFactory():
    """Creates XML elements using the '.' operator"""

    def __init__(self):
        pass

    def __getattribute__(self, name) -> XMLElement:
        return XMLElement(name)


_ = XMLElementFactory()
"""Convenience shortcut for writing ``_.div['bla']`` instead of ``XMLElement('div')['bla']``"""
