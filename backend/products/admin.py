from django.contrib import admin


# Register your models here.
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Product Information", {"fields": ["title", "price", "content"]})
        ]


admin.site.register(Product, ProductAdmin)
