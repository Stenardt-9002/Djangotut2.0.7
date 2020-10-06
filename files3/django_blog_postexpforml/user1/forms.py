
#create own forms

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = False) #default true
    class Meta:
        model = User #interact create user
        #fileds to shwo in form and in what order
        fields = ['username','email','password1','password2']



#add user data by user

class UsrrUpdateForm(forms.ModelForm):
    # emial = forms.EmailField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']


class ProffileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['imagefiled']
