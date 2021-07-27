"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitteruser import views as user_views
from authentication import views as a_views
from tweet import views as t_views
from notification import views as n_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', t_views.display_tweets, name='home'),
    path('post_tweet/', t_views.post_new_tweet, name='post_tweet'),
    path('login/', a_views.login_twit, name='login'),
    path('logout/', a_views.logout_twit, name='logout'),
    path('createuser/', a_views.create_new_twit_user, name='create_user'),
    path('follow/<int:other_id>/', user_views.follow),
    path('unfollow/<int:other_id>/', user_views.unfollow),
    path('notifications/', n_views.display_notifications, name='notifications'),
    path('<str:user_name>/', user_views.user_profile),
    path('tweet/<int:tweet_id>/', t_views.view_specific_tweet),
]

