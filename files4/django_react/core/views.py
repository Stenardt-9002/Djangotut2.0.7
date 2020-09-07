from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProductform, EditProduct
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


def render_change_data(request):
    # initial_data = {
    #     'title':
    # }
    # obj_jet = Product.objects.

    form = EditProduct(request.POST)
    # context = {
    #     "senor_form":form
    #            }
    if form.is_valid():

        # if request.method == "POST":
        idval = form.cleaned_data.get("id")
        print(idval)
        obj1 = Product.objects.get(id=(int)(idval))

        print(obj1)
        form = ProductForm(instance=obj1)
        if request.method == "POST":
            print("Kirsten Dunst")

            if form.is_valid():
                print("The phoque")
                form.save()

    context = {
        "senor_form": form
    }

    # return render(request,"core/product_create.html" ,context)
    return render(request, "core/product_detail.html", context)

    pass


def dynamic_lookup_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
        pass
    context = {
        "object": obj
    }

    # return render(request,"products/product_detail.html",context)
    return render(request, "core/product_detail.html", context)

    # except:


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()

        pass
    context = {
        "object": obj
    }

    return render()

    pass
