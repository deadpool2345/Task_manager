from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.fields import EmailField
from django.contrib.auth.models import User

class Signupform(UserCreationForm):
  email  = forms.EmailField()
  
  
  class meta:
    model = User
    fields = ['email']
