from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def register(request):
    # no nooed to create orm to match
    # html forms for Us
    print(request.method)
    print("niggAES")
    if request.method == 'POST':
        print("check reached here in POST")

        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            messages.success(request,f'Account succesful after form valdidation {username}')
            #redirection when successful
            print("check reached here")

            return redirect('blogpost-home')
            # return HttpResponse('<h1>OK</h1>')
            #put messasge in base1
    else:
        form1 = UserCreationForm()
    return render(request,'user1/register.html',{'form':form1})



# diiferent messages
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
