from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length = 50, null = False)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null= True)
    startdate = models.DateField()
    address = models.CharField(max_length = 100,null = True)
    enddate = models.DateField()
    starttime = models.TimeField()
    endtime = models.TimeField()
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return str(self.name)

class Eventprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_user = models.BooleanField(null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Eventprofile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.eventprofile.save()