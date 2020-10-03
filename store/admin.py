from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_filter = ['category']
    search_fields = ['name']


admin.site.register(Product,ProductAdmin)