from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ProductForm
from .models import Product


def product_create_view(request):
    context = {}

    return render(request,"core/product_detail.html",context)











    # form = ProductForm(request.POST or None)
    #
    # print(request.GET)
    # print(request.POST)
    # if form.is_valid():
    #     print("REACHED ")
    #     form.save()
    #     form = ProductForm()
    #
    #
    #
    # context = {
    #     'form':form
    # }
    #
    # return render(request,"core/product_detail.html",context)


# def product_detail_view(request):
#     obj = Product.objects.get(id = 1)
#     context = {
#         'object':obj
#     }
#
#     return render(request,"products/product_detail.html",context)











