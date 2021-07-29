from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import TwitUser
from tweet.models import Tweet

def user_profile(request, user_name):
  profile = TwitUser.objects.get(username=user_name)
  count = profile.following.count()
  follow_list = profile.following.all()
  tweets = Tweet.objects.filter(posted_by = profile.id)
  tweet_count = len(tweets)
  if request.user.is_authenticated:
    logged_in_follow_lst = request.user.following.all()
  else:
    logged_in_follow_lst = []
  return render(request, "profile.html", 
  {'profile': profile, 'count': count, 'tweets': tweets, 'tweet_count': tweet_count, 'follow_list': follow_list, "req_user_list": logged_in_follow_lst})


def follow(request, other_id):
  me = request.user
  me.following.add(other_id)
  me.save()
  if request.META:
        base = request.META['HTTP_REFERER']
        url = f'{base}'
        return HttpResponseRedirect(url)
  else:
        return HttpResponseRedirect(reverse('home'))


def unfollow(request, other_id):
  me = request.user
  me.following.remove(other_id)
  me.save()
  if request.META:
        base = request.META['HTTP_REFERER']
        url = f'{base}'
        return HttpResponseRedirect(url)
  else:
        return HttpResponseRedirect(reverse('home'))


def display_users(request):
  users = TwitUser.objects.all()
  return render(request, "users.html", {'users': users})