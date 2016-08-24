from django.contrib import admin
from .models import Post, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_number', 'title', 'description', 'image_file', 'created_at']

admin.site.register(Post)
admin.site.register(Product, ProductAdmin)
