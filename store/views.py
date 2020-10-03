from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)



def product(request):
    return render(request, 'store/product.html')


def contact(request):
    return render(request, 'store/contact.html')


def check_out(request):
    return render(request, 'store/checkout.html')