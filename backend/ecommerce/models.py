from django.db import models
from accounts.models import CustomUser


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    category = models.CharField(max_length=30)
    quantity = models.CharField(max_length=20)

class Order(models.Model):
    total_price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    shipping_address = models.URLField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')