"""django_blog_postexpforml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from user1 import views as user_viwes

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('blogs/', include('blogpost.urls')),
    path('', include('blogpost.urls')),
    path('register-user/',user_viwes.register,name = 'register'),
    path('login-user/',auth_views.LoginView.as_view(template_name = 'user1/login.html'),name = 'login'),
    path('logout-user/',
        auth_views.LogoutView.as_view(template_name = 'user1/logout.html'),
        name='logout'),
    path('password-reset-user/', auth_views.PasswordResetView.as_view(template_name = 'user1/password1_reset.html'), name='password_reset'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'user1/password1_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-user/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'user1/password1_reset_done.html') ,
         name='password_reset_done'),

path('password-reset-user-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'user1/password1_reset_confirm.html') ,
         name='password_reset_confirm'),


    path('profile-user/', user_viwes.profile, name='profile'),

    #default view login in



]
              # +static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


# only add if debug mode
# if settin:
    # pass
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
