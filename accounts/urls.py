from django.conf.urls import url
from django.contrib import admin
from django.urls import path 
from .import views
urlpatterns = [

    path(r"signup/",views.signup,name='signup'),
    path("login/",views.user_login,name="login"),
    path("logout/",views.logout,name="logout"),
    
]