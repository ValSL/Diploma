from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'amount', 'group']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
        }