from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length = 50, null = False)

    def __str__(self):
        return str(self.name)

class Business_Offering(models.Model):
    name = models.CharField(max_length = 50, null = False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Customer(models.Model):
    name = models.CharField(max_length = 50, null = False)

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    offer = models.ForeignKey(Business_Offering, on_delete=models.CASCADE, default = -1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default = -1)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, default = -1)
    order_date = models.DateField(default = datetime.datetime.now())
    fulfillment_date = models.TimeField(default = datetime.datetime.now())


# Create your models here.
