# Permissions and Groups in Django

## Custom Permissions
Custom permissions have been added to the `Article` model:
- `can_view`: View articles.
- `can_create`: Create articles.
- `can_edit`: Edit articles.
- `can_delete`: Delete articles.

## Groups
Three groups have been created with the following permissions:
- **Viewers**: `can_view`.
- **Editors**: `can_view`, `can_create`, `can_edit`.
- **Admins**: `can_view`, `can_create`, `can_edit`, `can_delete`.

## Enforcing Permissions
Permissions are enforced in views using the `@permission_required` decorator. For example:
```python
@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_view(request):
    # View logic here
