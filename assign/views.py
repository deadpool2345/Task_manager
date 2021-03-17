from django.shortcuts import render
from django.http import HttpResponse
'''
from assign.models import Task
from django.contrib.auth import get_user_model

User = get_user_model()

u1=User.objects.filter(username='phani').first()
task_1=Task.objects.filter(name='Dashboard creation').first()
task_2=Task.objects.filter(name='Converting pdf to html pages').first()

users=[i for i in User.objects.all()]
tasks=[i for i in Task.objects.all()]

user_task_dict={}

print(users[2])

for j in users:
    task_true=[]
    for i in tasks: 
        if j in i.users.all():
            task_true.append(i)
        user_task_dict[j.username]=task_true

print(user_task_dict)
'''

def login(request):
    return HttpResponse('Hello Phani')





