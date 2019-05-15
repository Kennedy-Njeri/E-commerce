from django.urls import path
from .views import item_list, products, checkout


urlpatterns = [
    path('', item_list, name='item_list'),
    path('products/', products, name='products'),
    path('checkout/', checkout, name='checkout'),


]