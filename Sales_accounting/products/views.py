from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Purchase
from .forms import ProductCreateForm, PurchaseCreateForm, ProductGroupCreateForm
from django.contrib.auth.decorators import login_required
from sales.models import Sale


@login_required
def product_list(request):
    products = Product.objects.filter(created_user=request.user.profile)
    return render(request, 'products/product_list.html', {'products': products, 'section': 'products'})


@login_required
def purchase_list(request):
    purchases = Purchase.objects.filter(created_user=request.user.profile)
    return render(request, 'products/purchase_list.html', {'purchases': purchases, 'section': 'purchases'})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product})


def product_create(request):
    # import pdb
    # pdb.set_trace()
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_user = request.user.profile
            form.save()
        return redirect('products:product_list')
    else:
        form = ProductCreateForm()
        return render(request, 'products/proudct_create.html', {'form': form})


def product_delete(request, id):
    product_for_delete = Product.objects.get(id=id)
    product_for_delete.delete()
    return redirect('products:product_list')


def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            product_amount = form.cleaned_data['amount']
            purchase_price = form.cleaned_data['purchase_price']
            instance.full_purchase_price = product_amount * purchase_price
            product = form.cleaned_data['product']
            product.amount += product_amount
            instance.created_user = request.user.profile
            product.save()
            form.save()
            return redirect('products:purchase_list')
        return render(request, 'products/purchase.html', {'form': form})
    else:
        form = PurchaseCreateForm()
        return render(request, 'products/purchase.html', {'form': form})


def product_group_create(request):
    if request.method == 'POST':
        form = ProductGroupCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.created_user = request.user.profile
            form.save()
            return redirect('products:product_create')
        return render(request, 'products/product_group_create.html', {'form': form})
    else:
        form = ProductGroupCreateForm()
        return render(request, 'products/product_group_create.html', {'form': form})


def overview(request):
    sum_sales = 0
    sum_purchases = 0
    if request.method == 'GET':
        all_sales = Sale.objects.filter(created_user=request.user.profile)
        all_purchases = Purchase.objects.filter(created_user=request.user.profile)
        for sale in all_sales:
            sum_sales += sale.final_price
        for pur in all_purchases:
            sum_purchases += pur.full_purchase_price
        profit = sum_sales - sum_purchases
    return render(request, 'products/overview.html', {'profit': profit})
