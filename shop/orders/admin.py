from django.contrib import admin, messages
from orders import models
from orders.models import InvalidOrderStateError


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem



@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_date', 'state']
    inlines = [OrderItemInline]
    exclude = ['state']
    action = ['review', 'accept', 'reject', 'ship', 'deliver', 'drop']
    readonly_fields = ['state']

    def transfer_state(self, newstate, request, queryset):
        for order in queryset:
            try:
                method = getattr(order, newstate)
                method()
            except InvalidOrderStateError as e:
                self.message_user(request, str(e), messages.WARNING)
            order.save()

    def review(self, request, queryset):
        self.transfer_state(request, 'review', queryset)
    def accept(self, request, queryset):
        self.transfer_state(request, 'accept', queryset)
    def reject(self, request, queryset):
        self.transfer_state(request, 'reject', queryset)
    def ship(self, request, queryset):
        self.transfer_state(request, 'ship', queryset)
    def deliver(self, request, queryset):
        self.transfer_state(request, 'deliver', queryset)
    def drop(self, request, queryset):
        self.transfer_state(request, 'drop', queryset)


@admin.register(models.PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    pass