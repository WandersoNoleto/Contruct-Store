from django import forms

from inventory.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'amount', 'price_buy', 'price_sell']
