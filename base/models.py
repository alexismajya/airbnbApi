from django.db import models

# Create your models here.

class Accommodation(models.Model):
    description= models.CharField(max_length=200)
    guests= models.IntegerField(max_length=200)
    region= models.CharField(max_length=200)
    created= models.DateTimeField(auto_now_add=True)

class Room(models.Model):
    guests= models.IntegerField(max_length=200)
    roomType= models.CharField(max_length=200)
    beds= models.IntegerField(max_length=200)
    accId = models.ForeignKey(Accommodation, default =1, verbose_name="Accommodation", on_delete=models.SET_DEFAULT)
    created= models.DateTimeField(auto_now_add=True)
