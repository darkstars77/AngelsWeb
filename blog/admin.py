from django.contrib import admin
from .models import Post, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_number', 'title', 'description', 'image_file', 'Product_satisfaction_by11st', 'pricePos',
                    'priceNeg', 'deliveryPos', 'deliveryNeg', 'sizePos', 'sizeNeg', 'extraPos', 'extraNeg',
                    'created_at']

admin.site.register(Post)
admin.site.register(Product, ProductAdmin)
