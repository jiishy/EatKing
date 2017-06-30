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
