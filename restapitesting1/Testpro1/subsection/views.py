from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Data_article

from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Data_article.objects.all()
        # get all article objects
        serialiseobj = ArticleSerializer(articles, many=True)

        # passing into serialiser class

        return JsonResponse(serialiseobj.data, safe=False)
        # return Json data
        pass


    elif request.method == "POST":
        data = JSONParser().parse(request)
        # get data post
        serialzerobj = ArticleSerializer(data=data)
        # create new object Serialiser
        if serialzerobj.is_valid():
            # valid
            serialzerobj.save()
            # save
            return JsonResponse(serialzerobj.data, status=201)
            # 201 success
            pass
        return JsonResponse(serialzerobj.errors)

    pass

# Create your views here.
