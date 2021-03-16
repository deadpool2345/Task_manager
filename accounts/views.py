from accounts.forms import Signupform
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout as user_logout
from .forms import Signupform
# Create your views here.

def signup(request):
  if request.method =="POST":
    form  = Signupform(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      print(username,password)
      user = authenticate(username=username ,password=password)
      print(user)
      login(request,user)
      return redirect ('login')

  else:
    form = Signupform()
  return render(request,"signup.html",{"form":form})       

def user_login(request):
  #username = request.POST['username']
  #password = request.POST['password']
  #user =authenticate(request,username =username,password=password )
  if request.method == "POST":
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request,username=username ,password=password)
      login(request,user)
      return redirect('login')
  else:       
    form = AuthenticationForm()
  
  return render(request,'login.html',{"form":form})
  

def logout(request):
  user_logout(request)
  return redirect('login')
