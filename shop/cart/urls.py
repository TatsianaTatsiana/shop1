from django.urls import path

from cart import views

urlpatterns = [
    path('', views.CartView.as_view(),
         name='cart_view'),
    path('item/remove/<int:pk>', views.CartItemRemoveView.as_view(),
         name='cart_item_remove'),
]