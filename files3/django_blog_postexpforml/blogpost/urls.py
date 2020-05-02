from user1 import views as user_viwes
from django.contrib import admin
from django.urls import path
from . import views as blogview
# from . import views
urlpatterns = [
    # path('', views.home,name='blogpost-home'), #name should be generic //geting empty string
    path('post/<int:pk>/', blogview.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', blogview.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', blogview.PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', blogview.PostCreateView.as_view(), name='post-create'),
    path('', blogview.PostListView.as_view(),name='blogpost-home'),
    path('user/<str:username>', blogview.UserPostListView.as_view(),name='user-posts'),
    path('about/',blogview.about,name = 'blogpost-about'),
    # path('register-user/',user_viwes.register,name = 'register'),
]
