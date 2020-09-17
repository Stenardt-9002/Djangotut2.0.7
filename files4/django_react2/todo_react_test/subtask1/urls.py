from django.urls import path,include
from django.views.generic import TemplateView
from . import  views
urlpatterns = [
    path('',views.apiTesting,name = "api-testing"),
    path('task-list',views.taskList,name = "api-task-listem"),
    path('task-detail/<str:pk>',views.specificTask,name = "api-task-showemone"),

]
