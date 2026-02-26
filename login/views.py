from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
import pandas as pd
from django.contrib.auth.decorators import login_required
import os

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request,"home.html")

def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Not a Valid User")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            messages.error(request,"Password Doesnt Match")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Already exists")
            return redirect('register')
        else:
            User.objects.create_user(username=username,email=email,password=password)
            messages.success(request,"Successfully Registered")
            return redirect('login')
    return render(request,'register.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.method=='POST':
        old_password=request.POST['old_password']
        new_password=request.POST['new_password']

        if not request.user.check_password(old_password):
            messages.error(request,"Old password entered was incorrect")
            return redirect('change_password')
        request.user.set_password(new_password)
        request.user.save()
        messages.success(request,"Password has been updated")
        return redirect('login')
    return render(request,"change_password.html")


def excel_data(request):
    file_path=os.path.join(settings.BASE_DIR,'media','Workstream.csv')
    df=pd.read_csv(file_path)
    data=df.values.tolist()
    columns=df.columns.tolist()
    context={
        "columns":columns,
        "data":data
    }
    return render(request,"data.html",context)