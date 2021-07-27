from django.shortcuts import render
from .models import Notification


def display_notifications(request):
  notifications = Notification.objects.filter(notify=request.user.username)
  notify_user = list(notifications)
  notifications.delete()
  return render(request, 'notification.html', {'notifications': notify_user})
