from django.db import models
from django.db import models
# Create your models here.
class Items(models.Model):
    itemname=models.CharField(max_length=20)
    itemcolor=models.CharField(max_length=15)
    itemprice=models.CharField(max_length=20)
