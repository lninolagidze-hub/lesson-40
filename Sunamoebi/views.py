from django.shortcuts import render
from django.db.models import Count
from .models import Product, Category


def home(request):
    products = Product.objects.all().order_by('price')

    categories = Category.objects.annotate(
        product_count=Count('product')
    ).filter(product_count__gt=0)

    return render(
        request,
        'Sunamoebi/home.html',
        {
            'products': products,
            'categories': categories,
        }
    )
    
def category_products(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category).order_by('price')

    return render(
        request,
        'Sunamoebi/category_products.html',
        {
            'category': category,
            'products': products,
        }
    )
    
def discounted_products(request):
    products = Product.objects.filter(
        has_discount=True
    ).order_by('price')

    return render(
        request,
        'Sunamoebi/discounted_products.html',
        {
            'products': products,
        }
    )