"""A minimal API for defining ACL protected resources and querying permissions"""

import functools
import typing

import flask


class AclResource:
    def __init__(self,
                 name: str,
                 rank: int = 1,
                 children: typing.Optional[typing.List['AclResource']] = None):
        """
        A resource that is protected by an acl

        Args:
            name: An identifier of the resource, must be unique among its parents
            rank: How to sort entries within siblings
            description: An optional help text
            children: A list of sub-entries
        """
        self.name = name
        self.rank = rank
        self.children = []
        self.parent = None
        if children:
            for child in children:
                self.add_child(child)

    def add_child(self, child: 'AclResource'):
        self.children.append(child)
        child.set_parent(self)

    def set_parent(self, parent: 'AclResource'):
        """Sets the parent of the entry"""
        self.parent = parent

    def __repr__(self):
        return '<AclResource "' + self.name + '">'


def current_user_has_permission(resource: AclResource) -> bool:
    """
    Whether the current user is allowed to access a specific resource.
    """
    return current_user_has_permissions([resource])[0][1]


def current_user_has_permissions(resources: [AclResource]) -> [[AclResource, bool]]:
    """
    Determines whether the currently logged in user has permissions for a list of resources.
    Implement actual behavior by patching the function.
    """
    return map(lambda resource: [resource, True], resources)


def current_user_email():
    """
    Returns the email address of the currently logged in user.
    Implement actual behavior by patching the function.
    """
    return 'guest@localhost'


def user_has_permission(email: str, resource: AclResource) -> bool:
    """
    Whether a user is allowed to access a specific resource.
    """
    return user_has_permissions(email, [resource])[0][1]


def user_has_permissions(email: str, resources: [AclResource]) -> [[AclResource, bool]]:
    """
    Determines whether a user has permissions for a list of resources.
    Implement actual behavior by patching the function.
    """
    return map(lambda resource: [resource, True], resources)


def require_permission(resource: AclResource, do_abort: bool = True,
                       abort_message="Sorry, but you don't have enough permissions to view this page.",
                       return_message="Not enough permissions.") \
        -> typing.Callable:
    """
    A decorator for protecting a resource by acl

    Args:
        resource: The resource for which user permissions are required
        do_abort: When true, a http exception is raised if the the user does not have permission
                      (useful when protecting whole pages).
                  When false, a small error message is returned (useful for ajax handlers).
        abort_message: The text of the "permission denied" http exception
        return_message: The text of the returned "permission denied" inline content

    Returns: The wrapped function
    """

    def decorator(f):
        def wrapper(*args, **kwargs):
            if not current_user_has_permission(resource):
                if do_abort:
                    flask.abort(403, abort_message)
                else:
                    return inline_permission_denied_message(return_message)

            else:
                return f(*args, **kwargs)

        functools.update_wrapper(wrapper, f)

        return wrapper

    return decorator


def inline_permission_denied_message(message="Not enough permissions"):
    """Returns a an inline html element that signals insufficient permissions"""
    return f'<span style="font-style:italic;color:#aaa"><span class="fa fa-lock"> </span> {message}</span>'
