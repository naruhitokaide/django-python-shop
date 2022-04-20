from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default= 1)
    device = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)