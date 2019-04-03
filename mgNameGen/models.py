from django.db import models
import os

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length = 100)
    imagePath = models.ImageField(upload_to ='testLoad',default="")
    
    def filename(self):
        return self.imagePath.name