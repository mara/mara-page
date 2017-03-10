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
    Implement actual behavior by patching the function.

    Args:
        resource: A resource to check

    Returns:
        True/False
    """
    return True


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


def require_permission(resource: AclResource, do_abort: bool = True) -> typing.Callable:
    """
    A decorator for protecting a resource by acl

    Args:
        resource: The resource for which user permissions are required
        do_abort: When true, a http exception is raised (useful when protecting whole pages).
                  When false, a small error message is return (useful for ajax handlers).

    Returns: The wrapped function
    """

    def decorator(f):
        def wrapper(*args, **kwargs):
            if not current_user_has_permission(resource):
                if do_abort:
                    flask.abort(403, "You don't have enough permissions to view this page.")
                else:
                    return '<span class="fa fa-lock" style="font-style:italic;color:#888"> Not enough permissions.</span>'

            else:
                return f(*args, **kwargs)

        functools.update_wrapper(wrapper, f)

        return wrapper

    return decorator
