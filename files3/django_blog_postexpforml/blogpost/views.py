from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog home</h1>')


def about(request):
    print("OOnga")
    print(request)
    return HttpResponse('<h1>About Page of this shiz</h1>')
