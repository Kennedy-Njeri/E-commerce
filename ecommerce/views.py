from django.shortcuts import render
from .models import Item
from django.views.generic import ListView, DetailView



class HomeView(ListView):
    model = Item
    template_name = "home-page.html"
    context_object_name = "items"

class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"
    context_object_name = "item"




def item_list(request):
    context = {
        'items' : Item.objects.all()
    }

    return render(request, "home-page.html", context)


def checkout(request):
    return render(request, "checkout-page.html")



def products(request):
    context = {
        'items': Item.objects.all()
    }

    return render(request, "product-page.html", context)