from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
import re
from twitteruser.models import TwitUser
from .forms import LoginTwitUserForm, CreateTwitUserForm


def create_new_twit_user(request):
  if request.method == 'POST':
    form = CreateTwitUserForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if TwitUser.objects.filter(username=data['username']).exists()==False:
        invalid_username = re.findall('\W', data['username'])
        if not invalid_username:
          if data['password1'] == data['password2']:
            TwitUser.objects.create_user(
              username=data['username'],
              first_name=data['first_name'],
              last_name=data['last_name'],
              email=data['email'],
              password=data['password1']
            )
            twitUser = authenticate(username=data['username'], password=data['password1'])
            login(request, twitUser)
            return HttpResponseRedirect(reverse('home'))
          else:
            return render(request, 'form.html', {'form': form, 'title': 'Create New Account', 'message': 'Passwords do not match'})
        else:
          return render(request, 'form.html', {'form': form, 'title': 'Create New Account', 'message': 'Username invalid, please only use letters, numbers or _. Spaces and special characters are not allowed'})
      else:
        return render(request, 'form.html', {'form': form, 'title': 'Create New Account', 'message': 'That username already exists'})
  form = CreateTwitUserForm()
  return render(request, 'form.html', {'form': form, 'title': 'Create New Account'})


def login_twit(request):
  if request.method == "POST":
    form = LoginTwitUserForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if TwitUser.objects.filter(username=data['username']).exists():
        twitUser = authenticate(username=data['username'], password=data['password'])
        login(request, twitUser)
        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
      else:
        return render(request, 'form.html', {'form': form, 'title': 'Login Page', 'message': 'If you already have an account, please verify that you are using correct login credentials. If you do not have an account, please create one'})
  form = LoginTwitUserForm()
  return render(request, 'form.html', {'form': form, 'title': "Login Page"})

def logout_twit(request):
  logout(request)
  return HttpResponseRedirect(reverse('home'))
