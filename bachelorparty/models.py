from django.db import models
from django.contrib.auth.models import User

class Broseph(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    attendance_details = models.TextField(blank = True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

# Create your models here.
