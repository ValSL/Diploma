from django.db import models


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
