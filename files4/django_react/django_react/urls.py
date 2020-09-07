"""django_react URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from pagesinfo import views
from pagesinfo.views import contact_view
from core.views import product_create_view,render_change_data,dynamic_lookup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name = 'home' ),
    # path('admin/',)
    path('contact/',contact_view),
    path('create/',product_create_view),
    path('edit/',render_change_data),
    path('products/<int:id>/',dynamic_lookup_view,name = 'product' ),

]
