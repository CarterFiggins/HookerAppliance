from django.db import models
import datetime
from django.utils import timezone



class Card(models.Model):
    modleNumber = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    applianceType = models.CharField(max_length= 50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.modleNumber
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    


class Appliance(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    serialNumber = models.CharField(max_length=200)
    unitCost = models.FloatField(default=0)
    Class = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.serialNumber