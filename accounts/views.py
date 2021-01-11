from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method == "POST":
        FisrtName = request.POST['firstname']
        LastName = request.POST['lastname']
        Username = request.POST['username']
        Email = request.POST['username']
        Password_1 = request.POST['password1']
        Password_2 = request.POST['password2']
        if Password_1 == Password_2:
            if User.objects.filter(username=Username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, "email id already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=FisrtName, last_name=LastName, username=Username,
                                                email=Email, password=Password_1)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request, "password not match")
            return redirect('register')
    else:
        return render(request, 'registration.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "user name and password not match")
            return redirect('login')
    else:
        return render(request, 'loginpage.html')


def logout(request):
    auth.logout(request)
    return redirect('/')