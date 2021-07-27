from twitteruser.models import TwitUser
from django.db import models

class Notification(models.Model):
  notify = models.CharField(max_length=150)
  message = models.CharField(max_length=140)
  sent_by = models.ForeignKey(TwitUser, on_delete=models.CASCADE, related_name='user_that_sent_notification')
  
  def __str__(self):
    return self.message
