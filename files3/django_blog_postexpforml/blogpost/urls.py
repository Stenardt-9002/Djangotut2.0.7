from user1 import views as user_viwes
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blogpost-home'), #name should be generic //geting empty string
    path('about/',views.about,name = 'blogpost-about'),
    # path('register-user/',user_viwes.register,name = 'register'),
]
