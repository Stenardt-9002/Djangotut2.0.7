from django import template
from core.models import Order
# from ../core.models import Order
import os

# from
register = template.Library()


# check authentication

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Order.objects.filter(user=user, ordered=False)

        # if query exist
        if qs.exists():
            return qs[0].items.count()

        return 0

    pass
