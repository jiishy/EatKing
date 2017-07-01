from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
	try:
		user = User.objects.create_user(username=username, password=password)

		return redirect('login')
	except:
		return redirect('signup')
@login_required
def logout(request):
	auth.logout(request)
	return redirect('login')
def user(request):
	return redirect('user')
def modify(request):
	return redirect('modify')
def modify_submit(request):
	legal = 1;# needs a function to judge the submited info is legal
	if not legal:
		return render(request,'modify')
	return render(request,'user')