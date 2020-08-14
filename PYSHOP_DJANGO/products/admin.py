from django.contrib import admin
from .models import Products,Offers


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'product_stock')


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Offers, OffersAdmin)