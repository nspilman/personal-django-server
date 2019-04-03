from django.db import models

# Create your models here.
class PDF(models.Model):
    name = models.CharField(max_length = 100, null = False)
    url = models.FileField(upload_to='pdfs')

    def __str__(self):
        return self.name