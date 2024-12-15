from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
#from .models import Post
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="acting_user")  # Who did the action
    verb = models.CharField(max_length=255)  # Describes the action (e.g., "liked your post")
    target_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)  # Track if the notification is read or not

    def __str__(self):
        return f"Notification for {self.recipient.username}: {self.verb}"