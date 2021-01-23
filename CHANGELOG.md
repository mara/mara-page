# Changelog

## 1.6.0 (2020-01-23)

- Include all versioned package files in wheel (not only python files)

## 1.5.0 - 1.5.2 (2020-10-14)

- Add travis integration and PyPi upload
- Fix Typerror with unconfigured permissions


## 1.4.0 - 1.4.1 (2019-02-12)

- Require Python >= 3.6
- Add new function `acl.user_has_permissions`
- Provide default implementations for `acl.user_has_permission` and `acl.current_user_has_permission` based on their plural forms
- Move some imports into the functions that use them in order to improve loading speed

## 1.3.0 (2018-03-19)

- Add separate function `inline_permission_denied_message` to unify inline "permission denied" messages


## 1.2.3 (2018-01-23)

- Add parameter `div_id` to functoin `asynchronous_content` + minor changes


## 1.2.2 (2018-01-23)

- implement hashing of navigation entries 


## 1.2.1 (2017-12-20)

- page rendering experience improvement: function `html.asynchronous_content` now sets the height of the placeholder diff to the previous height from local storage


## 1.2.0 (2017-12-09)

- many refactorings
- delayed rendering of html in `response.Response`
- performance improvements in `xml` module
- improved html markup in `bootstrap.card` and `bootstrap.table`
- new function `bootstrap.button`
- custom "permission denied messages" in `acl.require_permission`
- new function `html.asynchronous_content` for loading parts of a page throug ajax
- new function `html.highlight_syntax' based on pygments

**required changes**

- `bootstrap.card` has a new signature, please adapt calls


## 1.1.0 (2017-05-16) 

- Added functions for creating boostrap cards and tables
- Navigation entries can be hidden by setting `.visible = False`


## 1.0.1

- Added function `user_has_permission` to acl interface


## 1.0.0 (2017-03-08) 

- Initial version

