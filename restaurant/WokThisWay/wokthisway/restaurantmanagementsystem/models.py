from django.db import models
from django.utils import timezone

# Create your models here.
class Food(models.Model):
	ID=models.BigIntegerField(primary_key=True)
	Course=models.CharField(max_length=50)
	Cuisine=models.CharField(max_length=50)
	Name=models.CharField(max_length=50)
	Description=models.CharField(max_length=200)
	Price=models.FloatField()

def __str__(self):
	return self.Name

