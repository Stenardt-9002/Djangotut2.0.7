from django.db import models


# Create your models here.
class Product(models.Model):
    """docstring forProduct."""
    title = models.CharField(max_length = 120)
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default = ' This is cool ')

    # d
