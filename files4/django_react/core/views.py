from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ProductForm
from .models import Product


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        print("REACHED KAJASS")
        form.save()



    context = {
        'form':form
    }

    return render(request,"core/product_detail.html",context)


# def product_detail_view(request):
#     obj = Product.objects.get(id = 1)
#     context = {
#         'object':obj
#     }
#
#     return render(request,"products/product_detail.html",context)











