from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView, ListView

from catalog.forms import ItemSortForm, ItemFilterForm
from catalog.models import Item


class FilterListView(ListView):
    model = None
    sort_form = None
    filter_form = None
    default_sort_field = None

    def get_queryset(self):
        request = self.request
        item_sort_form = self.sort_form(request.GET)
        item_filter_form = self.filter_form(request.GET)

        self.item_sort_form = item_sort_form
        self.item_filter_form = item_filter_form

        filters = {
            k: v for (k, v) in
            item_filter_form.cleaned_data.items()
            if v is not None
        } if item_filter_form.is_valid() else {}
        order_by = ((item_sort_form.cleaned_data['order_by'] or self.default_sort_field)
                                         if item_sort_form.is_valid() else self.default_sort_field)


    def item_list(request: HttpRequest):
        item_sort_form = ItemSortForm(request.GET)
        item_filter_form = ItemFilterForm(request.GET)

        filters = {
            k: v for (k, v) in
            item_filter_form.cleaned_data.items()
            if v is not None
        } if item_filter_form.is_valid() else {}

        return self.model.objects.filter(**filters)\
                .order_by(order_by)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update(item_sort_form =self.item_sort_form,
            item_filter_form=self.item_filter_form)
        return context

class ItemListView(ListView):
    template_name = 'item_list.html'
    model = Item
    sort_form = ItemSortForm
    filter_form = ItemFilterForm
    default_sort_field = 'name'

class ItemDetailView(DetailView):
    template_name = 'item_detail.html'
    queryset = Item.objects.filter(count__gt=0)