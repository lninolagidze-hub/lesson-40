from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'category',
            'odor_type',
            'has_discount',
            'discount_rate',
        ]