from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .forms import ProductCreateForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product})


def product_create(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('products:product_list')
    else:
        form = ProductCreateForm()
        return render(request, 'products/proudct_create.html', {'form': form})


def product_delete(request, id):
    product_for_delete = Product.objects.get(id=id)
    product_for_delete.delete()
    return redirect('products:product_list')
