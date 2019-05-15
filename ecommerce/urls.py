from django.urls import path
from .views import item_list, products, checkout, HomeView, ItemDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),


]