from django.urls import path
from .views import index, product, contact, check_out,cart ,update_cart

app_name = 'store'

urlpatterns = [
    path('',index, name='index'),
    path('product/<slug:slug>',product, name='product'),
    path('cart/',cart, name='cart'),
    path('update-cart/',update_cart, name='update_cart'),
    path('contact/',contact, name='contact'),
    path('checkout/',check_out, name='checkout'),

]
