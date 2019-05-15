from django.urls import path
from .views import item_list, products, checkout, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('products/', products, name='products'),
    path('checkout/', checkout, name='checkout'),


]