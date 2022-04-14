from django.contrib import admin
from . models import Category, Brand, Image, Product

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Image)