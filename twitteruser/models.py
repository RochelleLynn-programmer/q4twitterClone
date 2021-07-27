from django.db import models
from django.contrib.auth.models import AbstractUser

class TwitUser(AbstractUser):
  following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='followed_by_users')

  def __str__(self):
      return self.username
