from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
import re
from .models import Tweet
from twitteruser.models import TwitUser
from notification.models import Notification
from .forms import TweetForm


@login_required
def display_tweets(request):
  a_tweet = Tweet.objects.filter(posted_by=request.user)
  f_tweets = Tweet.objects.filter(posted_by__in = request.user.following.all())
  combined = a_tweet.union(f_tweets).order_by('-date_posted')
  notification_count = Notification.objects.filter(notify=request.user.username).count()
  return render(request, 'homepage.html', {'combined': combined, 'notify': notification_count})


# How to filter with two query set objects
# https://stackoverflow.com/questions/29587382/how-to-add-an-model-instance-to-a-django-queryset/43544410

def post_new_tweet(request):
  if request.method=='POST':
    form = TweetForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Tweet.objects.create(
        tweet = data['tweet'],
        posted_by = request.user
      )
      notify = re.findall('@(\w+)', data['tweet'])
      if notify:
        try:
          TwitUser.objects.get(username=notify[0])
          Notification.objects.create(
            notify = notify[0],
            message = data['tweet'],
            sent_by = request.user
          )
        except:
          return HttpResponseRedirect(reverse('home'))
      return HttpResponseRedirect(reverse('home'))
  form = TweetForm()
  return render(request, 'form.html', {'form': form, 'title': 'Post Your Tweet'})


def view_specific_tweet(request, tweet_id):
  tweet = Tweet.objects.get(id=tweet_id)
  return render(request, 'tweet.html', {'tweet': tweet})