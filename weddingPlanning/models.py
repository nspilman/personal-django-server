from django.db import models

class Guest(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)

class Hotel(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length=200)
    distance = models.DecimalField(default = 1, decimal_places = 2, max_digits = 4)

    def __str__(self):
        return self.name

class Food(models.Model):
    pass


# Create your models here.
