
# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='blog-name'), #name should be generic //geting empty string
    path('about/',views.about,name = 'blog-about')
]
