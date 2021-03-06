from django.db import models
from products.models import Product
from django.core.exceptions import ValidationError
from account.models import Profile


class Sale(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    final_price = models.IntegerField()
    buyer = models.ForeignKey('counterparties.Counterparty', on_delete=models.CASCADE, related_name='sales', null=True)
    created_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sales', null=True)



