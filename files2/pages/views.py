from django.http import HttpResponse
from django.shortcuts import render

def homepage(*args,**kwargs):
    return HttpResponse("<h1> Hello world </h1>")

def contct_view(*arg,**kwargs):
    return HttpResponse("<h1> contact page  </h1>")
    pass
# Create your views here.
