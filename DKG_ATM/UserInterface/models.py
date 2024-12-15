from django.db import models
from BankInterface.models import Account  # Import the Account model

class UserInterface(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    # account = models.OneToOneField(Account, on_update=models.CASCADE)
      # Create a one-to-one relationship with Account

    def __str__(self):
        return self.account.card_number  # Use card_number from the linked Account model
