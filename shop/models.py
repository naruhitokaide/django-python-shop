from distutils.command.upload import upload
from itertools import product
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
        
        
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Image(models.Model):
    image = models.ImageField(upload_to = 'products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    def __str__(self):
        return f"{self.product}"