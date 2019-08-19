from django.contrib import admin

# Register your models here.
from cart import models

class CartItemInline(admin.TabularInline):
    model = models.CartItem
    fields = ['item', 'amount']
    extra = 1
    ordering = ['item__name', 'item__price']


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ['user']
    list_display = ['id', 'username']
    list_filter = ['user__username']
    inlines = [CartItemInline]
    actions = ['remove_all_items']

    def remove_all_items(self, request, queryset):
        for cart in queryset:
            cart.items.all().delete()
    remove_all_items.short_description = "Remove all items in the carts"

    def username(self, cart):
        return (
            cart.user.username if cart.user is not None
            else '- Unknown -'
        )

#второй вариант
'''admin.site.register(Cart)'''
# отделяет компаратор contain или может отделять username, который находится в user