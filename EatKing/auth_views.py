from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from EatKing.models import CustomUser
from django.shortcuts import get_object_or_404

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
    image = request.FILES.get('image')
    email = request.POST.get('email')
    is_superuser = 0
    try:
        user = CustomUser.objects.create_user(username=username, password=password, email=email, like_shop_num=0,image=image)
        if user:
            user.save
            return redirect('login')
    except:
        return redirect('signup')

def modify(request):
    u = get_object_or_404(CustomUser, pk=request.user.id)
    return render(request, 'modify.html', { 'u' : u })

def modify_submit(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    image = request.FILES.get('image')
    try:
        user = get_object_or_404(CustomUser, pk=request.user.id)
        if user:
            user.username = username
            user.set_password(password)
            user.email = email
            user.image = image
            user.save()
            user = auth.authenticate(request, username=username, password=password)
            if not user:
                return redirect('login')
            auth.login(request, user)
            return redirect('user')
    except:
        return redirect('modify')

def user(request):
    u = get_object_or_404(CustomUser, pk=request.user.id)
    return render(request, 'user.html', { 'u' : u })

@login_required
def logout(request):
	auth.logout(request)
	return redirect('login')
