from django.contrib import messages
from django.shortcuts import render, get_object_or_404

# auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


def checkout(request):
    return render(request, "checkout.html")


class HomeView(ListView):
    model = Item
    paginate_by = 4
    template_name = "home.html"
    # conversion to class view


class OrderSummaryView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        # get order details
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary1.html', context)

        except ObjectDoesNotExist:
            messages.error(self.request, "No active order was found")
            return redirect("/")

        pass

    # model = Order
    # template_name = 'order_summary1.html'
    pass


class ProductDetailView(DetailView):
    model = Item
    template_name = "products.html"


# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request, "home.html",context)

@login_required
def add_to_cart(request, slug):
    item1 = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item1,
        user=request.user,
        ordered=False

    )
    # query set of order
    order1 = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order1.exists():
        order2 = order1[0]

        if order2.items.filter(item__slug=item1.slug).exists():  # already in cart increment
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The quantity has been increased")

        else:
            order_item.quantity = 1
            order_item.save()

            messages.info(request, "this item was added to your cart")
            order2.items.add(order_item)
            pass


    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    # return redirect("core:order-summary", slug=slug)
    return redirect("core:order-summary")

    pass


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # set of order of user
    order1 = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order1.exists():
        order2 = order1[0]
        if order2.items.filter(item__slug=item.slug).exists():  # already in cart increment
            # removal of order
            # grab it then remoe it
            order_item = OrderItem.objects.filter(
                item=item
                , user=request.user, ordered=False
            )[0]
            # order_item.quantity+=1
            # order_item.save()

            # removal
            order2.items.remove(order_item)
            messages.info(request, "this item was removed from your cart")
            # return redirect("core:order-summary", slug=slug)
            return redirect("core:order-summary")



        else:
            # order2.items.add(order_item)
            # the user doesnt have an order
            messages.info(request, "this item was not in your cart")

            return redirect("core:product", slug=slug)
            pass

    else:
        messages.info(request, "You donot have an active order")
        return redirect("core:product", slug=slug)

    # return redirect("core:product",slug = slug)


@login_required
def remove_single_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    # set of order of user
    order1 = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order1.exists():
        order2 = order1[0]
        if order2.items.filter(item__slug=item.slug).exists():  # already in cart increment
            # removal of order
            # grab it then remoe it
            order_item = OrderItem.objects.filter(
                item=item
                , user=request.user, ordered=False
            )[0]
            # removal
            if order_item.quantity>1:
                order_item.quantity -= 1
                order_item.save()

            else:
                order2.items.remove(order_item)
                pass

                pass


            # order2.quantity -=1
            # order2.save()
            # order2.items.remove(order_item)
            messages.info(request, "this item quantity reduced and updated")
            return redirect("core:order-summary")


        else:
            # order2.items.add(order_item)
            # the user doesnt jave an order
            messages.info(request, "this item was not in your cart")

            return redirect("core:product", slug=slug)
            pass

    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)

    # return redirect("core:product",slug = slug)
