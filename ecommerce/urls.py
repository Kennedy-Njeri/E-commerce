from django.urls import path
from .views import (item_list,
                    products,
                    checkout,
                    HomeView,
                    ItemDetailView,
                    add_to_cart,
                    remove_from_cart,
                    OrderSummaryView
                    )


urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart')


]