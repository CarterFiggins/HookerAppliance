from django.db import models
import datetime
from django.utils import timezone



class Card(models.Model):
    modelNumber = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    applianceType = models.CharField(max_length= 50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.modelNumber
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    


class Appliance(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    serialNumber = models.CharField(max_length=200)
    unitCost = models.FloatField(default=0)
    Class = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    dateSold = models.CharField(max_length=200)
    purchaser = models.CharField(max_length=200)
    ticketNum = models.IntegerField(default = 0)
    sellingPrice = models.FloatField(default=0)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.serialNumber