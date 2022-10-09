from django.db import models
from .utils import get_random_string


# Create your models here.


class Wallet(models.Model):
    wallet_types = [
        ('Visa', 'Visa'),
        ('Mastercard', 'Mastercard')
    ]
    wallet_currencies = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('RUB', 'RUB')
    ]

    owner = models.ForeignKey('auth.User', related_name='wallets', on_delete=models.CASCADE)
    name = models.CharField(max_length=8, default=get_random_string, unique=True, editable=False)
    type = models.CharField(max_length=10, choices=wallet_types)
    currency = models.CharField(max_length=3, choices=wallet_currencies)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.created_on is None:
            if self.currency in ['USD', 'EUR']:
                self.balance = 3
            else:
                self.balance = 100
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
