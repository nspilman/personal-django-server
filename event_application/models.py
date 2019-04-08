from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 50, null = False)
    created_user = models.ForeignKey(User, on_delete="CASCADE", related_name="user", null= True)
    startdate = models.DateField()
    enddate = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

