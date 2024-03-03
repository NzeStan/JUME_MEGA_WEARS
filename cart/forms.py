# forms.py
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
PRODUCT_SIZE_CHOICES = [("S", "SMALL"), ("M", "MEDIUM"), ("L", "LARGE")]


class CartAddProductForm(forms.Form):
    size = forms.TypedChoiceField(
        choices=PRODUCT_SIZE_CHOICES,
        coerce=str,
        widget=forms.Select(
            attrs={
                "class": "form-select appearance-none bg-white border border-gray-300 hover:border-gray-500 px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            }
        ),
    )
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.Select(
            attrs={
                "class": "form-select appearance-none bg-white border border-gray-300 hover:border-gray-500 px-4 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            }
        ),
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
