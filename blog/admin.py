from django.contrib import admin
from .models import Post, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'image_file', 'filtered_image_file']

admin.site.register(Post)
admin.site.register(Product, ProductAdmin)
