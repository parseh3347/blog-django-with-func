from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def user_register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid() :
            cd = form.cleaned_data
            user= User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.firstname=cd['firstname']
            user.firstname=cd['lastname']
            user.is_staff=True 
            user.is_superuser=True
            user.save()
            messages.success(request,'user registertion successfully','success')
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request,'accounts/register.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'login is successfully..','success')
                return redirect('home')
            else:
                messages.error(request,'username and password is not correct ..', 'danger')
    else:
        form = UserLoginForm()
    return render(request , 'accounts/login.html', {'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, 'logged is successfully..','success')
    return redirect('home')
