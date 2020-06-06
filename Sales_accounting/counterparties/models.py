from django.db import models
from account.models import Profile


class Counterparty(models.Model):
    type_choises = [('suplier', 'Supplier'), ('buyer', 'Buyer')]
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    product_group = models.ManyToManyField('products.ProductGroup')
    balance = models.IntegerField(default=0)
    type = models.CharField(choices=type_choises, max_length=20)
    created_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='counterpartyes', null=True)

    def __str__(self):
        return self.name

