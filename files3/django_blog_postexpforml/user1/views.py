from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    # no nooed to create orm to match
    # html forms for Us
    print(request.method)
    print("niggAES")
    if request.method == 'POST':
        print("check reached here in POST")

        # form1 = UserCreationForm(request.POST)
        form1 = UserRegisterForm(request.POST)

        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            # lso known as “flash message
            messages.success(request,f'Account succesful after form valdidation {username}')
            messages.success(request,f'Your account has been created now go login')

            #redirection when successful
            print("check reached here")
            return redirect('login')
            # return redirect('blogpost-home')
            # return HttpResponse('<h1>OK</h1>')
            #put messasge in base1
    else:
        # form1 = UserCreationForm()
        form1 = UserRegisterForm()

    return render(request,'user1/register.html',{'form':form1})
    #fields filled along with error messgae



# diiferent messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error




#profile rendering when you are logged in
@login_required
def profile(request):
    return render(request,'user1/profile.html')
