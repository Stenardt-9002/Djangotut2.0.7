from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank = True,null = True)
    price = models.DecimalField(decimal_places = 2,max_digits = 10000)
    summary = models.TextField(default = "")

    def get_absolute_url(self):
        # return f"/products/{self.id}"
        return reverse("core:product-dyna" , kwargs = {"id":self.id})
    pass


# Create your models here.
