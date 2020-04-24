from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# sample based view data
post1 = [
    {
        'author': 'Ben',
        'title': 'How to destroy a franchise',
        'content': 'Warner Brothers are a sucks',
        'data_posted': 'July 20 2012'
    },
    {
        'author': 'Batman',
        'title': 'How to destroy a franchise',
        'content': 'Ben afflec and then weird vampire guy ,really? ',
        'data_posted': 'January 6 2017'
    }
]


def home(request):
    # contxt = {
    #     'posts':post1
    # }
    contxt = {
        'posts': Post.objects.all()
    }
    return render(request, 'blogpost/home1.html', contxt)
    # return HttpResponse('<h1>Blog home</h1>')


class PostListView(ListView):
    model = Post  # what model to query
    template_name = 'blogpost/home1.html'  # <app>/<model>_<viewtype>.html

    # name of var to loop over in html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # .models.py date-posted

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        pass

    """docstring for PostCreateView."""


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # required for ensuring that updating requires login
        form.instance.author = self.request.user
        return super().form_valid(form)
        pass

    def test_func(self):
        post_1 = self.get_object()
        if self.request.user == post_1.author:
            return True
        return False

        pass

    """docstring for PostUpdateView."""


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #go to home when you delete stuff
    def test_func(self):
        post_1 = self.get_object()
        if self.request.user == post_1.author:
            return True
        return False




def about(request):
    # print("OOnga")
    print(request)
    # return HttpResponse('<h1>About Page of this shiz</h1>')
    return render(request, 'blogpost/about1.html', {'title': 'About pAge'})
