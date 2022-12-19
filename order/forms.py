from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'email', 'phone', 'country', 'city', 'state', 'zip_code', ]
