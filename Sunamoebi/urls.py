from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('discounted/', views.discounted_products, name='discounted_products'),
    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),
    path(
    'add-product/',
    views.add_product,
    name='add_product'
    ),
    
        path(
        'update-product/<int:product_id>/',
        views.update_product,
        name='update_product'
    ),

    path(
    'delete-product/<int:product_id>/',
    views.delete_product,
    name='delete_product'
)
]



