from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.views import View
from django.core.paginator import Paginator

from .models import Product, Category, OdorType
from .forms import ProductForm


class HomeView(View):

    def get(self, request):

        # Start with all products
        products = Product.objects.all()

        # Get search, filter and sort values from URL
        search = request.GET.get('search', '').strip()
        category = request.GET.get('category', '')
        odor_type = request.GET.get('odor_type', '')
        discount = request.GET.get('discount', '')
        sort = request.GET.get('sort', 'price_asc')


        if search:
            products = products.filter(
                name__icontains=search
            )



        if category:
            products = products.filter(
                category_id=category
            )


        if odor_type:
            products = products.filter(
                odor_type_id=odor_type
            )



        if discount == 'yes':
            products = products.filter(
                has_discount=True
            )

        elif discount == 'no':
            products = products.filter(
                has_discount=False
            )

    
        if sort == 'price_asc':
            products = products.order_by('price')

        elif sort == 'price_desc':
            products = products.order_by('-price')

        elif sort == 'name_asc':
            products = products.order_by('name')

        elif sort == 'name_desc':
            products = products.order_by('-name')

 

        paginator = Paginator(products, 2)

        page_number = request.GET.get('page')

        page_obj = paginator.get_page(page_number)



        categories = Category.objects.annotate(
            product_count=Count('product')
        ).filter(
            product_count__gt=0
        )

    

        odor_types = OdorType.objects.all()

     

        return render(
            request,
            'Sunamoebi/home.html',
            {
                'products': page_obj,
                'categories': categories,
                'odor_types': odor_types,

                'search': search,
                'selected_category': category,
                'selected_odor_type': odor_type,
                'selected_discount': discount,
                'selected_sort': sort,
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