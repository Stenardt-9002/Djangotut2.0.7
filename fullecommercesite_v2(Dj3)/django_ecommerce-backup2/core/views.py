from django.shortcuts import render,get_object_or_404
from .models import Item,OrderItem,Order
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Item
    template_name = "home.html"
    # conversion to class view


class ProductDetailView(DetailView):
    model = Item
    template_name = "products.html"


# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "home.html",context)


def add_to_cart(request, slug):
    item1 = get_object_or_404(Item,slug = slug)
    order_item,created = OrderItem.objects.get_or_create(
                             item = item1,
                             user=request.user,
                             ordered=False

    )
    order1 = Order.objects.filter(
                                    user = request.user,
                                    ordered=False
                                  )
    if order1.exists():
        order2 = order1[0]

        if order2.items.filter(item__slug = item1.slug).exists():
            order_item.quantity+=1
            order_item.save()
        else:
            order2.items.add(order_item)
            pass


    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user = request.user,ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product",slug = slug)


    pass



