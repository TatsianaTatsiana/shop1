from django import forms


class ItemSortForm(forms.Form):
    order_by = forms.ChoiceField(choices=[
        ('name', 'Name'),
        ('-name', 'Name (Z-A)'),
        ('price', 'Price'),
        ('-price', 'Price (high to low)'),
        ('count', 'count'),
    ], label='Order', required=False)


class ItemFilterForm(forms.Form):
    name__contains = forms.CharField(
        max_length=200,
        required=False,
        label='Name')
    price__gt = forms.DecimalField(
        max_digits=30,
        decimal_places=2,
        required=False,
        label='Price greater than'
    )
    price__lt = forms.DecimalField(
        max_digits=30,
        decimal_places=2,
        required=False,
        label='Price less than'
    )