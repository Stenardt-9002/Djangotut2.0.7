from django.urls import path
from .views import (
    products,
    checkout,
    ProductDetailView,
    HomeView,
    add_to_cart
)

app_name = 'core'

urlpatterns = [
    # path('', home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    # path('products/', products, name='products')
    path('products/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart')
]
