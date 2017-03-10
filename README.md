# Mara page

Minimal API for defining pages of Flask-based backends independently from the actual backend infrastructure.
 
When a web app is spread across many independent Flask blueprints, then this library can be used to add

- navigation entries
- page titles 
- resource-based ACL protection
- page-specific CSS and JS files

without having access to a global layout or the Flask app. 


The library provides a drop-in werkzeug ``Response`` class that is enriched with additional information that a 
backend can use to render the final html page.
  
## Example

This is a simple web ui for displaying the current time:
 
```python
"""Clock UI"""

import flask
from awesome_clock import clock
from mara_page import acl, navigation, response, _

# The flask blueprint that handles
awesome_clock = flask.Blueprint('awesome_clock', __name__, url_prefix='/clock', static_folder='static')

# Defines an ACL resource (needs to be handled by the application)
acl_resource = acl.AclResource('Clock')

# Defines a part of the navigation tree (needs to be handled by the application)
navigation_entry = navigation.NavigationEntry(
    label='Awesome clock', icon='clock-o', description='Something that tells the time',
    children=[
        navigation.NavigationEntry(
            label='What time is it now?', uri_fn=lambda: flask.url_for('awesome_clock.clock_page') + '#1',
            icon='question-circle', description='Should be able to display the current time'),

        navigation.NavigationEntry(
            label='And now?', uri_fn=lambda: flask.url_for('awesome_clock.clock_page') + '#2',
            icon='refresh', description='For the impatient'),
    ])


# Defines the '/clock' page
@awesome_clock.route('')
@acl.require_permission(acl_resource)  # Requires permission to the 'Clock' resource
def clock_page():
    return response.Response(
        # The actual page content (can be also a call to `flask.render_template`
        # or anything else that produces a string)
        html=_.div[_.h1['What time is it now?'],
                   _.p['The current time is ', str(clock.what_time_is_it_now())],
                   _.img(src=flask.url_for('awesome_clock.static', filename='cuckoo-clock.jpg'),
                         style='max-width:100%')],
        # The page title
        title='Awesome clock',

        # Action buttons
        action_buttons=[
            response.ActionButton('javascript:location.reload()', 'Refresh', 'Refresh clock', 'refresh'),
            response.ActionButton('javascript:location.reload()', 'Update', 'Refresh clock', 'clock-o')
        ],

        # CSS files to be added to the html head
        css_files=[flask.url_for('awesome_clock.static', filename='clock.css')],

        # Javascript files to be added to the bottom of the html body
        js_files=[flask.url_for('awesome_clock.static', filename='clock.js')]
    )
```

It is up to the actual Flask app to define how to render such a response and what to do with the ACL resources and navigation entries. 
The [mara app](https://github.com/mara/mara-app) will render the response like this:

![Example backend](docs/awesome-clock.png)


