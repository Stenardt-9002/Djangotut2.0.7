from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
post1 = [
{
    'author':'Ben',
    'title':'How to destroy a franchise',
    'content':'Warner Brothers are a sucks',
    'data_posted':'July 20 2012'
},
{
    'author':'Batman',
    'title':'How to destroy a franchise',
    'content':'Ben afflec and then weird vampire guy ,really? ',
    'data_posted':'January 6 2017'
}
]




def home(request):
    contxt = {
        'posts':post1
    }
    return render(request,'blogpost/home1.html',contxt)
    # return HttpResponse('<h1>Blog home</h1>')



def about(request):
    print("OOnga")
    print(request)
    # return HttpResponse('<h1>About Page of this shiz</h1>')
    return render(request,'blogpost/about1.html' ,{'title':'Abootututu'})
