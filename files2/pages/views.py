from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("<h1> Hello world </h1>")
    return render(request,"home.html",{})

def contct_view(request):
    return HttpResponse("<h1> contact page  </h1>")

# Create your views here.

def about_view(request):
    my_context = {
        "my_text":"this is about us",
        "my_nu" : 123,
        "my_lit" : [12,34,45,56,312],
        "my_htm" : "<h1> This is sent from view </h1>",

    }
    # return HttpResponse("<h1> About Page </h1> ")
    return render(request,"about.html",my_context)

def social_view(request):
    return HttpResponse("<h1> Social Page </h1>")
