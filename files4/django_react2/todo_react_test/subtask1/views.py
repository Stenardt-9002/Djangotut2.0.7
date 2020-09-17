from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerialiser
from .models import Task


# Create your views here.

@api_view(['GET'])
def apiTesting(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    # return JsonResponse("REACHED A VIEW", safe=False)
    return Response(api_urls)

    pass

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerialiser(tasks, many=True)
    return Response(serializer.data)

    # return Response()




@api_view(['GET'])
def specificTask(request,pk):
    tasks = Task.objects.get(id= pk)
    serializer = TaskSerialiser(tasks, many=False)
    return Response(serializer.data)

    # return Response()





