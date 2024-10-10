from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    event_id = models.AutoField(primary_key=True, default=1)
    event_name = models.CharField(max_length=100)
    event_venue = models.CharField(max_length=100)
    event_start_time = models.DateTimeField()
    event_end_time = models.DateTimeField()


    def __str__(self):
        return self.event_name


class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')

class Us(models.Model):
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    branch = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    section = models.CharField(max_length=10)
    university = models.CharField(max_length=100)

class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"

from django.db import models

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    lecturer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
