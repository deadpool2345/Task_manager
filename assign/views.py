from django.shortcuts import render,redirect
from django.http import HttpResponse
from assign.models import Task
from django.contrib.auth import get_user_model
from .forms import CreateUserForm,TaskCreationForm
from django.contrib.auth import authenticate,login,logout

User = get_user_model()

users=[i for i in User.objects.all()]
tasks=[i for i in Task.objects.all()]

def task_with_status():
    tasks=[i for i in Task.objects.all()]
    task_div_status={'assigned':[],'ongoing':[],'completed':[]}
    for i in tasks:
        if i.status=='O':
            task_div_status['ongoing'].append(i)
        elif i.status=='A':
            task_div_status['assigned'].append(i)
        else:
            task_div_status['completed'].append(i)
    return task_div_status

def task_with_details():
    tasks=[i for i in Task.objects.all()]
    task_user_dict={}
    for i in tasks:
        user_obj_list=[]
        user_obj_list=i.users.all()
        user_name_list=[j.username for j in user_obj_list]
        task_user_dict[str(i.id)]=user_name_list
    return task_user_dict

#print(type(task_user_dict['4']))

def register(request):
    form=CreateUserForm()

    if request.method=='POST':
        form = CrearteUserForm(request.POST)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'assign/register.html',context)

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        print(user)
        if user:
            login(request,user)
    return render(request,'assign/login.html')

def task_creation(request):
    form=TaskCreationForm()
    if request.method=="POST":
        form=TaskCreationForm(request.POST)
        if form.is_valid():
            forminst = form.save(commit=False)
            print(form.cleaned_data['users'])
            forminst.assigner = request.user
            forminst.save()
            form=TaskCreationForm()
    context={'form':form}
    return render(request,'assign/task_create.html',context)


def display_tasks(request):
    task_div_status=task_with_status()
    context={
        'tasks':task_div_status
    }
    return render(request,'assign/task_home.html',context)

def display_task_details(request,id):
    task_user_dict=task_with_details()
    context={
        'tasks':tasks,
        'id':int(id),
        'task_users':task_user_dict[id]
    }
    return render(request,'assign/task_details.html',context)
    




