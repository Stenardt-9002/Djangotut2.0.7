from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.reg
admin.site.register(Post)