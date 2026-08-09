from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.views import View

from .models import Product, Category
from .forms import ProductForm


class HomeView(View):

    def get(self, request):

        products = Product.objects.all().order_by('price')

        categories = Category.objects.annotate(
            product_count=Count('product')
        ).filter(
            product_count__gt=0
        )

        return render(
            request,
            'Sunamoebi/home.html',
            {
                'products': products,
                'categories': categories,
            }
        )


class CategoryProductsView(View):

    def get(self, request, category_id):

        category = get_object_or_404(
            Category,
            id=category_id
        )

        products = Product.objects.filter(
            category=category
        ).order_by('price')

        return render(
            request,
            'Sunamoebi/category_products.html',
            {
                'category': category,
                'products': products,
            }
        )


class DiscountedProductsView(View):

    def get(self, request):

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


class ProductDetailView(View):

    def get(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        return render(
            request,
            'Sunamoebi/product_detail.html',
            {
                'product': product,
            }
        )


class AddProductView(View):

    def get(self, request):

        form = ProductForm()

        return render(
            request,
            'Sunamoebi/add_product.html',
            {
                'form': form,
            }
        )

    def post(self, request):

        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        return render(
            request,
            'Sunamoebi/add_product.html',
            {
                'form': form,
            }
        )


class UpdateProductView(View):

    def get(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        form = ProductForm(
            instance=product
        )

        return render(
            request,
            'Sunamoebi/update_product.html',
            {
                'form': form,
                'product': product,
            }
        )

    def post(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        form = ProductForm(
            request.POST,
            instance=product
        )

        if form.is_valid():
            form.save()

            return redirect(
                'product_detail',
                product_id=product.id
            )

        return render(
            request,
            'Sunamoebi/update_product.html',
            {
                'form': form,
                'product': product,
            }
        )


class DeleteProductView(View):

    def get(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        return render(
            request,
            'Sunamoebi/delete_product.html',
            {
                'product': product,
            }
        )

    def post(self, request, product_id):

        product = get_object_or_404(
            Product,
            id=product_id
        )

        product.delete()

        return redirect('home')