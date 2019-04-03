from django.db import models

class Post(models.Model):
    title = models.CharField(max_length = 100,default = "", null = True)
    imagePath = models.ImageField(upload_to ='testLoad',default="")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField(default = '')
    
    def filename(self):
        return self.imagePath.name

    def __str__(self):
        return str(self.title) + ',' + str(self.date)
# Create your models here.
