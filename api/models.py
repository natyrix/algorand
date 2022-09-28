from pyexpat import model
from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

class Assets(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    asset_index = models.CharField(max_length=255)