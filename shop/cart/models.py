from django.conf import settings
from django.db import models

# Create your models here.
from catalog.models import ItemAmount


class CartItem(ItemAmount):
    cart = models.ForeignKey('Cart',
                             on_delete=models.CASCADE,
                             related_name='items')


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True, default=None,
                                on_delete=models.CASCADE)

    @property
    def total_price(self):
        return sum(item.total_price
                   for item in self.items.all())

    def __str__(self):
        username = (
            self.user.username if self.user is not None
        else '- Unknown -'
        )
        return "Cart #{} for user {}".format(self.id, self.user.username)