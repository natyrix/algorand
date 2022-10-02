from pyexpat import model
from urllib import request
from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    has_requested = models.BooleanField(default=False)
    request_status = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
       return self.first_name +" "+ self.last_name

class Assets(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    asset_index = models.CharField(max_length=255)
    asset_name = models.CharField(max_length=255, default="None")
    asset_status = models.BooleanField(default=False)
    image_url = models.CharField(max_length=255, default="None")
    ipfs_url = models.CharField(max_length=255, default="None")

    # def __str__(self):
    #    return self.first_name + self.last_name