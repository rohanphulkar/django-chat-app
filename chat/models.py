from django.db import models
from accounts.models import User
import uuid
from django.utils import timezone
class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    name = models.UUIDField(default=uuid.uuid4,editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="owner")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user")

    def __str__(self):
        return self.owner.email

class Chat(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="room")
    content = models.CharField(max_length=255,blank=True, null=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.localtime(timezone.now()))

    class Meta:
        ordering = ('-date_added',)