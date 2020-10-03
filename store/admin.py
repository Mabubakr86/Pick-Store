from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
