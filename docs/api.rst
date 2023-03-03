API
===

.. module:: mara_page

This part of the documentation covers all the interfaces of Mara Page. For
parts where the package depends on external libraries, we document the most
important right here and provide links to the canonical documentation.


ACL
---

.. module:: mara_page.acl

.. autoclass:: AclResource
    :special-members: __init__
    :members:

.. autofunction:: current_user_has_permission

.. autofunction:: current_user_has_permissions

.. autofunction:: current_user_email

.. autofunction:: user_has_permission

.. autofunction:: user_has_permissions

.. autofunction:: require_permission

.. autofunction:: inline_permission_denied_message


Bootstrap
---------

.. module:: mara_page.bootstrap

.. autoclass:: ActionButton
    :special-members: __init__
    :members:

.. autofunction:: card

.. autofunction:: table

.. autofunction:: button


HTML
----

.. module:: mara_page.html

.. autofunction:: highlight_syntax

.. autofunction:: spinner

.. autofunction:: spinner_js_function

.. autofunction:: asynchronous_content


Navigation
----------

.. module:: mara_page.navigation

.. autoclass:: NavigationEntry
    :special-members: __init__
    :members:


Response
--------

.. module:: mara_page.response

.. autoclass:: Response
    :special-members: __init__
    :members:


XML
---

.. module:: mara_page.xml

.. autoclass:: XMLElement
    :special-members: __init__, __call__, __getitem__, __str__
    :members:

.. autofunction:: render

.. autoclass:: XMLElementFactory
    :special-members: __init__, __getattribute__
    :members:

    A singletone factory is available at `mara_page._`
