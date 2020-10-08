from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import ReviewForm


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)



def product(request, slug):
    product = Product.objects.get(slug=slug)
    # product_reviews = ProductReviw.objects.filter(product=product)
    last_reviews = ProductReviw.objects.get_last_reviews(prod=product)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():

            form_data = review_form.save(commit=False)
            form_data.reviewer = request.user
            form_data.product = product
            form_data.save()
            return redirect(reverse('store:product', kwargs={'slug':product.slug}))
    else:
        review_form = ReviewForm


    return render(request, 'store/product.html', {'product':product,
                            'r_form':review_form, 'reviews':last_reviews})


def contact(request):
    return render(request, 'store/contact.html')


def check_out(request):
    return render(request, 'store/checkout.html')