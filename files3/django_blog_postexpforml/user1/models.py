from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

# field for profile feature

class Profile(models.Model):
    """docstring for Profile."""
    # uer1 = models.OneToOneField(uer1,on_delete = models.CASCADE )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # imagefiled = models.ImageField(default='default.jpg',upload_to='profile_dir')
    imagefiled = models.ImageField(default='defaul1t.png', upload_to='profile_dir')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def __init__(self, arg):
    #     super(Profile, self).__init__()
    #     self.arg = arg
    # override a method
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)  # running parent
        img = Image.open(self.imagefiled.path)
        #check size
        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.imagefiled.path)

        pass
