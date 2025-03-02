class RoleMixin:
    """Mixin for user roles."""
    def __init__(self):
        self.roles = set()

    def add_role(self, role):
        """Assign a role to the user."""
        pass

    def remove_role(self, role):
        """Remove a role from the user."""
        pass

    def show_roles(self):
        """Display all roles assigned to the user."""
        pass


class PermissionMixin:
    """Mixin for user permissions."""
    def __init__(self):
        self.permissions = set()

    def grant_permission(self, action):
        """Grant a specific permission to the user."""
        pass

    def revoke_permission(self, action):
        """Revoke a permission from the user."""
        pass

    def check_permission(self, action):
        """Check if the user has a specific permission."""
        pass


class User:
    """Base user class."""
    def __init__(self, name):
        self.name = name
        super().__init__()


class AdminUser(User, RoleMixin, PermissionMixin):
    """Admin user with full control over roles and permissions."""
    def __init__(self, name):
        super().__init__(name)


class EditorUser(User, RoleMixin, PermissionMixin):
    """Editor user with limited permissions."""
    def __init__(self, name):
        super().__init__(name)


class ViewerUser(User, RoleMixin):
    """Viewer user with read-only access."""
    def __init__(self, name):
        super().__init__(name)
