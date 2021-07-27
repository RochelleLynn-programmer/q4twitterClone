from django.db import models
from twitteruser.models import TwitUser
from django.utils import timezone


class Tweet(models.Model):
  tweet = models.CharField(max_length=140)
  posted_by = models.ForeignKey(TwitUser, on_delete=models.CASCADE)
  date_posted = models.DateTimeField(default= timezone.now)

  def __str__(self):
    return self.tweet
