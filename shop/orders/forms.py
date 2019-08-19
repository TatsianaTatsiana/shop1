from django import forms

from orders import models


class NewOrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        exclude = ['state', 'created_date']