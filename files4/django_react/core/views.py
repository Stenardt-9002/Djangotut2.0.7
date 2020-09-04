from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ProductForm, RawProductform
from .models import Product


def product_create_view(request):
    # form = RawProductform()
    # if request.method == "POST":
    #     form = RawProductform(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         Product.objects.create(**form.cleaned_data)
    #         form = RawProductform()
    #         pass
    #     else:
    #         print(form.errors)
    #
    # context = {"senor_form": form}
    #
    # return render(request, "core/product_detail.html", context)

    form = ProductForm(request.POST or None)
    #
    print(request.GET)
    print(request.POST)
    if form.is_valid():
        print("REACHED ")
        form.save()
        form = ProductForm()

    context = {
        'senor_form': form
    }

    return render(request, "core/product_detail.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id = 1)
#     context = {
#         'object':obj
#     }
#
#     return render(request,"products/product_detail.html",context)
