from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category, ProductType,
    Attribute, AttributeValue, Product, ProductVariant
)

admin.site.register([
    ProductType,
    Attribute, AttributeValue
])

admin.site.register(Category, MPTTModelAdmin)

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    fields = ['sku', 'name', 'price']


class ProductAdmin(admin.ModelAdmin):
    # 指定 InlineAdmin
    inlines = [
        ProductVariantInline,
    ]


admin.site.register(Product, ProductAdmin)

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    fields = ['sku', 'name', 'price', 'quantity', 'quantity_allocated', 'images']