from django import forms
from .models import Sale
from django.forms import ValidationError


class SaleCreateForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['product', 'amount']

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        product = self.cleaned_data['product']
        if amount > product.amount:
            raise ValidationError('Too much amount!')
        return amount

