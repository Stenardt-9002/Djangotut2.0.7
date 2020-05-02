from django.shortcuts import render
from .models import Product



def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # automatically creates id
    #map all attribute s of obj
    # context = {
    #     'title' :obj.title,
    #     'description': obj.description,
    # }

    context = {
        'object' : obj,
    }
    return render(request,"products/detail.html",context)
