from django.db import models
from counterparties.models import Counterparty


class ProductGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    amount = models.IntegerField()
    group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name='product')

    def __str__(self):
        return f'{self.name}'


class Purchase(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    counterparty = models.ForeignKey(Counterparty, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    purchase_price = models.IntegerField(default=0)
    amount = models.IntegerField()

