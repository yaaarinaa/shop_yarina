from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products, 'title': 'Все товары'})

def recent_products(request):
    one_week_ago = timezone.now() - timedelta(days=7)
    products = Product.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')
    return render(request, 'shop/product_list.html', {'products': products, 'title': 'Новинки'})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})