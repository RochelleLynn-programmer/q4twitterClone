from django import forms
from django.forms.widgets import PasswordInput

class LoginTwitUserForm(forms.Form):
  username = forms.CharField(max_length=150)
  password = forms.CharField(widget = PasswordInput)


class CreateTwitUserForm(forms.Form):
  username = forms.CharField(max_length=150)
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  email = forms.EmailField()
  password1 = forms.CharField(widget=PasswordInput)
  password2 = forms.CharField(widget=PasswordInput)