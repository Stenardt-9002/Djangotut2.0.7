from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
# save database
class Post(models.Model):
    # create attribute
    title = models.CharField(max_length=100)
    content = models.TextField()  # unrestricted text
    # save data
    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)  # when user is delete what to do delete post

    def __str__(self):
        return self.title
