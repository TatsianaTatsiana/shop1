from django.db import models

# Create your models here.
from django.utils import timezone

from catalog.models import ItemAmount


class OrderItem(ItemAmount):
    order = models.ForeignKey('Order',
                              on_delete=models.CASCADE,
                              related_name='items')


class PaymentType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class InvalidOrderStateError(RuntimeError):
    pass


class Order(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    tel = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    STATES = [
        ('new', 'New order'),
        ('in review', 'in review'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
        ('shipping', 'shipping'),
        ('delivered', 'delivered'),
        ('dropped', 'dropped')
    ]
    state = models.CharField(max_length=20, choices=STATES, default='new')

    def review(self):
        if self.state == 'new':
            self.state = 'in review'
        elif self.state == 'in review':
            pass
        else:
            raise RuntimeError

    def accept(self):
        if self.state == 'in review':
            self.state = 'accepted'
        elif self.state == 'accepted':
            pass
        else:
            raise RuntimeError

    def reject(self):
        if self.state == 'in review':
            self.state = 'rejected'
        elif self.state == 'rejected':
            pass
        else:
            raise RuntimeError

    def ship(self):
        if self.state == 'accepted':
            self.state = 'shipping'
        elif self.state == 'shipping':
            pass
        else:
            raise RuntimeError

    def deliver(self):
        if self.state == 'shipping':
            self.state = 'delivered'
        elif self.state == 'delivered':
            pass
        else:
            raise RuntimeError

    def drop(self):
        if self.state == 'shipping':
            self.state = 'dropped'
        elif self.state == 'dropped':
            pass
        else:
            raise RuntimeError

    def __str__(self):
        return f'{self.last_name}, {self.first_name}, {self.tel}'




