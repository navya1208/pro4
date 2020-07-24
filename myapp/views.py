from django.shortcuts import render
from django.http import HttpResponse

import math
# Create your views here.

def index(requet):
  return HttpResponse('<center><h1>"Welcome to the app of myapp"</h1></center>')

def home(request):
  return render(request,"myapp/home.html",{'name':'Navya'})

def fact(request,n):
  n=int(n)
  return HttpResponse('<center><h1>The factorial of {} is <span style="color:green;">{}</span></h1></center>'.format(n,math.factorial(n)))