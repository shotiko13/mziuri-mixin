# mziuri-mixin
Davaleba



Step 1: Implement the Mixins

RoleMixin

Allows users to be assigned one or more roles.
add_role(role), remove_role(role), show_roles().

PermissionMixin

Allows users to have specific permissions (read, write, delete, etc.).
grant_permission(action), revoke_permission(action), check_permission(action).
Step 2: Implement the User Classes

AdminUser (inherits from RoleMixin, PermissionMixin)

Can assign roles & permissions to other users.

EditorUser (inherits from RoleMixin, PermissionMixin)

Has limited permissions (can only edit content).

ViewerUser (inherits from RoleMixin)

Can only view content and has no permissions to modify.