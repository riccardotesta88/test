from django.contrib import admin
from .models import Product,Order

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#
admin.site.register(Product)
admin.site.register(Order)