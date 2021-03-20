from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns=[
    path('tasks/',views.display_tasks,name='display_tasks'),
    path('tasks/<id>/',views.display_task_details,name='task_details'),
    path('register/',views.register,name='register'),
    path('task_create/',views.task_creation,name='task_create')
]