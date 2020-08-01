from django.conf import settings
from django.db import models
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    discout_price = models.FloatField(blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        # print("\n\n\nReached\n\n\n\n")
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug  # name in url
        })

    def get_remove_from_cart(self):
        return reverse("core:remove", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        # return self.title
        return f"{self.quantity} of {self.item.title} this is string"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.item.discout_price * self.quantity
        pass

    def get_amount_saved(self):
        return self.item.price - self.item.discout_price

    def get_final_price(self):
        if not self.item.discout_price:
            return self.get_total_item_price()
        return self.get_discount_item_price()
        pass


# the above string is shown in admin site when checking for items

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
        pass
