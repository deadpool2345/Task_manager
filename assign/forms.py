from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 

from django.forms import ModelForm
from .models import Task

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class TaskCreationForm(ModelForm):
    users=forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = User.objects.all()
               )
    class Meta:
        model = Task
        fields=['name','description','users']


