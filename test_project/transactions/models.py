from django.db import models


# Create your models here.

class Transaction(models.Model):
    creator = models.ForeignKey('auth.User', related_name='transactions', on_delete=models.CASCADE)
    sender = models.CharField(max_length=8)
    receiver = models.CharField(max_length=8)
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    status = models.CharField(editable=False, max_length=8, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

