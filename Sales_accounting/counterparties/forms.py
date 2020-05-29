from django import forms
from .models import Counterparty


class CounterpartiesForm(forms.ModelForm):
    class Meta:
        model = Counterparty
        fields = ['name', 'phone', 'email', 'product_group', 'type']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'product_group': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }
