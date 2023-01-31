from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import django.contrib.messages
from django.contrib import messages, auth


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            else:
                messages.info(request,"Invalid Credentials")
                return redirect("login")

        return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User Name already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return redirect('login')
                print("User Created")
        else:
            messages.info(request,"Password not matching")
            return render(request,'register.html')

        return redirect('/')
    return render(request,'register.html')