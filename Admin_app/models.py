from django.db import models
from django.utils import timezone
from datetime import datetime,date
# Create your models here.
class rider(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    createdAt = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class driver(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    DateOfBirth = models.DateField(default=date.today)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class ride(models.Model):
    first_name = models.ForeignKey(rider,default=1,on_delete = models.SET_DEFAULT)
    url = models.URLField(unique=True,default=1)
    date = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return self.Rider
