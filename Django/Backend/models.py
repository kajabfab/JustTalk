from __future__ import unicode_literals

from jsonfield import JSONField
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)

class ChatRoom(models.Model):
    location = models.CharField(max_length=100)
    chat_tree = JSONField()
