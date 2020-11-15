from django import template 
from ..models import Customer, Product, Order, OrderItem

register = template.Library() 

@register.simple_tag 
def get_cart_total(user):  # keyward arguments can be used (x=user)
    customer = Customer.objects.get(user=user)
    order, created = Order.objects.get_or_create(customer=customer)
    order_total = order.get_total_items_count
    return order_total

