from django.db import models

# Create your models here.
class UserInterface(models.Model):
    card_number = models.CharField(max_length=16)
    pin = models.CharField(max_length=4)

    def __str__(self):
        return self.card_number



