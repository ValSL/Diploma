from django.db import models
from products.models import Product
from django.core.exceptions import ValidationError


class Sale(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    final_price = models.IntegerField()


