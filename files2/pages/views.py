from django.http import HttpResponse
from django.shortcuts import render

def homepage(request,*args,**kwargs):
    # return HttpResponse("<h1> Hello world </h1>")
    return render(request,"home.html",{})

def contct_view(request,*arg,**kwargs):
    return HttpResponse("<h1> contact page  </h1>")

# Create your views here.

def about_view(request):
    return HttpResponse("<h1> About Page </h1> ")

def social_view(request):
    return HttpResponse("<h1> Social Page </h1>")
