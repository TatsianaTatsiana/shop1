from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cart.forms import AddToCartForm
from cart.models import Cart, CartItem

# Create your views here.
from catalog.models import Item


class CartItemRemoveView(View):
    def get(self, request, id: int):
        request.cart.items.filter(pk=id).delete()
        return redirect('cart_view')


class CartView(View):
    def post(self, request):
        add_to_cart_form = AddToCartForm(request.POST)
        cart = request.cart  # type: Cart

        if add_to_cart_form.is_valid():
            item = get_object_or_404(
                Item,
                pk=add_to_cart_form.cleaned_data['item_id'])
            cart.add_item(item,
                             add_to_cart_form.cleaned_data['amount'])

        return redirect('item_list')

    def get(self, request):
        return render(request, 'cart_list.html', {'cart': request.cart})






'''def get_cart(session):  а можно через создание middleware
    try:
        cart_id = session['cart_id']
        cart = Cart.objects.get(pk=cart_id)
    except (KeyError, Cart.DoesNotExist) as e:
        cart = Cart()
        cart.save()
        session['cart_id'] = cart.pk
    return cart'''
