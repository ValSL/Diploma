from django.db import models


class Counterparty(models.Model):
    type_choises = [('suplier', 'Supplier'), ('buyer', 'Buyer')]
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    product_group = models.ManyToManyField('products.ProductGroup')
    balance = models.IntegerField(default=0)
    type = models.CharField(choices=type_choises, max_length=20)

    def __str__(self):
        return self.name

