from django.shortcuts import render, redirect
from .forms import SaleCreateForm
from .models import Sale
from products.models import Product
from django.contrib import messages


def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'sales/sales_list.html', {'sales': sales, 'section': 'sales'})


def sale_create(request):
    if request.method == 'POST':
        form = SaleCreateForm(request.POST)
        if form.is_valid():
            new_sale = form.save(commit=False)
            new_sale.final_price = new_sale.product.price * new_sale.amount
            new_sale.save()
            current_product = Product.objects.get(id=new_sale.product.id)
            current_product.amount -= new_sale.amount
            current_product.save()
        return render(request, 'sales/sale_create.html', {'form': form})
    else:
        form = SaleCreateForm()
        return render(request, 'sales/sale_create.html', {'form': form})


