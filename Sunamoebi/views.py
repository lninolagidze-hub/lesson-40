from django.shortcuts import render
from django.db.models import Count
from .models import Product, Category
from .forms import ProductForm


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

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(
        request,
        'Sunamoebi/product_detail.html',
        {
            'product': product,
        }
    )

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ProductForm()

    return render(
        request,
        'Sunamoebi/add_product.html',
        {
            'form': form,
        }
    )

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)

    else:
        form = ProductForm(instance=product)

    return render(
        request,
        'Sunamoebi/update_product.html',
        {
            'form': form,
            'product': product,
        }
    )
    

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('home')

    return render(
        request,
        'Sunamoebi/delete_product.html',
        {
            'product': product,
        }
    )