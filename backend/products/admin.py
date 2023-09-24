""" Product admin
"""
from django.contrib import admin


# Register your models here.
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    """Manipulating the admin view of the Product model

    Args:
        admin (_type_): admin package from django.contrib
    """

    fieldsets = [
        ("Product Information", {"fields": ["title", "price"]}),
        ("Detailed Overview Of The Product", {"fields": ["content"]}),
    ]


admin.site.register(Product, ProductAdmin)
