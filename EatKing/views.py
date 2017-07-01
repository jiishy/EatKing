#from django.shortcuts import render
#from .models import *
#Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
	#posts = Post.objects.order_by('-created_at')
	return render(request, 'index.html')#, {'posts': posts})

def search(request):
	return render(request,'search.html')

def search_submit(request):
	#todo
	return render(request,'shop.html')

def filter(request):
	return render(request,'search.html')

def sort(request):
	return render(request,'search.html')

def enter_shop(request):
	return render(request,'shop.html')

def comment(request):
	return render(request,'shop.html')

def like_comment(request):
	return render(request,'shop.html')

def unlike_comment(request):
	return render(request,'shop.html')

def like_shop(request):
	return render(request,'shop.html')

def unlike_shop(request):
	return render(request,'shop.html')
