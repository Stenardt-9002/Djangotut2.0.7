from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Post


# sample based view data
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
    # contxt = {
    #     'posts':post1
    # }
    contxt = {
        'posts': Post.objects.all()
    }
    return render(request,'blogpost/home1.html',contxt)
    # return HttpResponse('<h1>Blog home</h1>')


class PostListView(ListView):
    model = Post
    template_name = 'blogpost/home1.html' #<app>/<model>_<viewtype>.html

    # name of var to loop over in html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #.models.py date-posted
    
    """docstring for PostListView."""

    # def __init__(self, arg):
    #     super(PostListView, self).__init__()
    #     self.arg = arg


class PostDetailView(DetailView):
    model = Post
    # rest all variable not set and django convention being follwed
    # template_name = 'blogpost/home1.html'  # <app>/<model>_<viewtype>.html
    #
    # # name of var to loop over in html
    # context_object_name = 'posts'
    # ordering = ['-date_posted']  # .models.py date-posted

    """docstring for PostDetailView."""


def about(request):
    # print("OOnga")
    print(request)
    # return HttpResponse('<h1>About Page of this shiz</h1>')
    return render(request,'blogpost/about1.html' ,{'title':'About pAge'})
