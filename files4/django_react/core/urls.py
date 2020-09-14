
from django.urls import path
from pagesinfo import views
from pagesinfo.views import contact_view
from .views import product_create_view,render_change_data,dynamic_lookup_view,product_delete_view,render_all_object


app_name = 'core'
urlpatterns = [
    path('create/',product_create_view),
    path('edit/',render_change_data),
    path('<int:id>/',dynamic_lookup_view,name = 'product-dyna' ),
    path('<int:id>/delete/', product_delete_view ,name='product-delete'),
    path('all',render_all_object,name = "all-products")

]
