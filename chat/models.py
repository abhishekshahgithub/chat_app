from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.
class Chatter(models.Model):
	# name = models.CharField(max_length=200)
	chat_field = models.CharField(max_length=400)
	sender = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name = 'sender_name')
	receiver = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

# class Sender(models.Model):
# 	sender = models.ForeignKey(settings.AUTH_USER_MODEL, default=1) 



