from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),

    path(
        'category/<int:category_id>/',
        views.CategoryProductsView.as_view(),
        name='category_products'
    ),

    path(
        'discounted/',
        views.DiscountedProductsView.as_view(),
        name='discounted_products'
    ),

    path(
        'product/<int:product_id>/',
        views.ProductDetailView.as_view(),
        name='product_detail'
    ),

    path(
        'product/add/',
        views.AddProductView.as_view(),
        name='add_product'
    ),

    path(
        'product/<int:product_id>/update/',
        views.UpdateProductView.as_view(),
        name='update_product'
    ),

    path(
        'product/<int:product_id>/delete/',
        views.DeleteProductView.as_view(),
        name='delete_product'
    ),

]


