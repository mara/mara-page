.. rst-class:: hide-header

Mara Page documentation
=======================

Welcome to Mara Page’s documentation. This is one of the core modules of the `Mara Framework <https://github.com/mara>`_
offering a minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure.

When a web app is spread across many independent Flask blueprints, then this library can be used to add

* navigation entries
* page titles
* resource-based ACL protection
* page-specific CSS and JS files
* without having access to a global layout or the Flask app.

The library provides a drop-in werkzeug ``Response`` class that is enriched with additional information that a backend can use to render the final html page.


User's Guide
------------

This part of the documentation focuses on step-by-step instructions how to use this extension.

.. toctree::
   :maxdepth: 2

   installation
   example


API Reference
-------------

If you are looking for information on a specific function, class or
method, this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


Additional Notes
----------------

Legal information and changelog are here for the interested.

.. toctree::
   :maxdepth: 2

   license
   changes