
#create own forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = False) #default true
    class Meta:
        model = User #interact create user
        #fileds to shwo in form and in what order
        fields = ['username','email','password1','password2']



    pass
