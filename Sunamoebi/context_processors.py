from .models import Product


def latest_products(request):
    products = Product.objects.order_by('-id')[:5]

    return {
        'latest_products': products
    }
    