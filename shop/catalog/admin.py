from django.contrib import admin

# Register your models here.
from catalog import models

class ItemPriceFilter(admin.SimpleListFilter):
    title = 'item price'
    parameter_name = "price"
    def lookups(self, request, model_admin):
        return [
            ('0-10', 'less than 10'),
            ('10-15', 'from 10 to 50'),
            ('50-', 'greater than 50')
        ]
    def queryset(self, request, queryset):
        price_range = self.value()

        price_ranges = {
            '0-10':{'price__lte': 10},
            '10-50':{'price__gt': 10, 'price__lte': 50},
            '50-':{'price__gt': 50}
        }

        filter = price_ranges.get(price_range,{})

        return queryset.filter(**filter)



@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = [ItemPriceFilter, 'count']

