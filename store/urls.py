from django.urls import path
from .views import index, product, contact, check_out

app_name = 'store'

urlpatterns = [
    path('',index, name='index'),
    path('product/<slug:slug>',product, name='product'),
    path('contact/',contact, name='contact'),
    path('checkout/',check_out, name='checkout'),

]
