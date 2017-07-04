from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from EatKing.models import CustomUser

def login(request):
	return render(request, 'login.html')

def authenticate(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(request, username=username, password=password)
	if not user:
		return redirect('login')
	auth.login(request, user)
	return redirect('index')

def signup(request):
	return render(request, 'signup.html')

def signup_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    id = request.POST.get('id')
    email = request.POST.get('email')
    is_superuser = 0
    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, like_shop_num=0)
        if user:
            user.save
            return redirect('login')
    except:
        return redirect('signup')

def modify(request):
    auth.modify(request)
    return redirect('modify')

def user(request):
    auth.user(request)
    return redirect('user')

@login_required
def logout(request):
	auth.logout(request)
	return redirect('login')

def modify_submit(request):
	legal = 1;# needs a function to judge the submited info is legal
	if not legal:
		return render(request,'modify')
	return render(request,'user')