from django.urls import path

from orders import views

urlpatterns = [
    path('add', views.OrderView.as_view(),
         name='order_add'),
]
