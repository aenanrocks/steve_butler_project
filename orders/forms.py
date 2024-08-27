# orders/forms.py

from django import forms
from .models import Order

# Creating a form for the Order model to handle order creation and updates
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Specifies that this form is for the Order model
        fields = ['details', 'notes', 'status', 'finish_date', 'delivery_method']  # The fields to be included in the form

    # Adding custom styling or attributes to form fields
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['details'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['finish_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['delivery_method'].widget.attrs.update({'class': 'form-control'})
