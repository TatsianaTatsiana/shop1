from django.urls import path

from catalog import views

urlpatterns = [
    path('item_list/', views.ItemListView.as_view(), name='item_list'),
    path('item_detail/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail')
]