from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import ReviewForm
from django.http import JsonResponse


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/products.html', context)



def product(request, slug):
    product = Product.objects.get(slug=slug)
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


def cart(request):
    context = {}
    render(request, 'store/cart.html', context=context)

def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        product = Product.objects.get(id=product_id)
        user = request.user
        customer = Customer.objects.get(user=user)
        order, created = Order.objects.get_or_create(customer=customer)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            order_item.quantity +=1
            order_item.save()
            order_total = order.get_total_items_count

        return JsonResponse(data={'order_total':order_total})
    return JsonResponse(data={'error':'error'})

def contact(request):
    return render(request, 'store/contact.html')


def check_out(request):
    return render(request, 'store/checkout.html')