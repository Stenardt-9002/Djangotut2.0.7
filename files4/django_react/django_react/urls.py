
from django.contrib import admin
from django.urls import path,include
from pagesinfo import views
from pagesinfo.views import contact_view
from core.views import product_create_view,render_change_data,dynamic_lookup_view,product_delete_view,render_all_object

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name = 'home' ),
    path('contact/',contact_view),
    path('products/',include('core.urls'))

]
