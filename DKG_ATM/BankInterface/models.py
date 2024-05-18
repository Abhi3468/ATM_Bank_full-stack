from django.db import models

# Create your models here.
# in atm_app/models.py
class Account(models.Model):
    account_number = models.CharField(max_length=16, unique=True)  # Assuming a maximum of 20 characters for the account number
    card_pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.account_number

class WithdrawalHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

class DepositHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


    