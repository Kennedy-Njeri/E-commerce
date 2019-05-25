from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone




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


def add_to_cart(request, slug):

    item = get_object_or_404(Item, slug=slug)

    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)

    order_qs = Order.objects.filter(user=request.user, ordered=False)


    if order_qs.exists():

        order = order_qs[0]


        #check if the order item is in the order
        if order.items.filter(item__slug=item.slug):
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)

    else:

        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)

    return redirect("product", slug=slug )


def remove_from_cart(request, slug):

    item = get_object_or_404(Item, slug=slug)

    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():

        order = order_qs[0]

        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():

            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]

            order.items.add(order_item)

        else:

            return redirect("product", slug=slug)


    else:

        return redirect("product", slug=slug)

    return redirect("product", slug=slug)




