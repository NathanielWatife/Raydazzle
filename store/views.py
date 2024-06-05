"""Views for Store"""
from django.shortcuts import render
from .models import Product


# Create your views here.
def store(request):
    """
        Views for store
    """
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)



def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)