from django.db import models

class Account(models.Model):
    card_number = models.CharField(max_length=16, unique=True)  # Renamed from account_number to card_number
    card_pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.card_number

class WithdrawalHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class DepositHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
