from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#field for profile feature

class Profile(models.Model):
    """docstring for Profile."""
    # uer1 = models.OneToOneField(uer1,on_delete = models.CASCADE )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # imagefiled = models.ImageField(default='default.jpg',upload_to='profile_dir')
    imagefiled = models.ImageField(default='defaul1t.png',upload_to='profile_dir')

    def __str__(self):
        return f'{self.user.username} Profile'



    # def __init__(self, arg):
    #     super(Profile, self).__init__()
    #     self.arg = arg
