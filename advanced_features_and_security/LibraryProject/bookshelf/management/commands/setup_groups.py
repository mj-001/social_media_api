from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from your_app_name.models import Article

class Command(BaseCommand):
    help = "Set up user groups and permissions"

    def handle(self, *args, **kwargs):
        # Define groups
        groups_permissions = {
            'Viewers': ['can_view'],
            'Editors': ['can_view', 'can_edit', 'can_create'],
            'Admins': ['can_view', 'can_edit', 'can_create', 'can_delete'],
        }

        # Get Article content type
        content_type = ContentType.objects.get_for_model(Article)

        for group_name, permissions in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm in permissions:
                permission = Permission.objects.get(codename=perm, content_type=content_type)
                group.permissions.add(permission)
                self.stdout.write(f"Added {perm} to group {group_name}")
        
        self.stdout.write("Groups and permissions setup completed.")
