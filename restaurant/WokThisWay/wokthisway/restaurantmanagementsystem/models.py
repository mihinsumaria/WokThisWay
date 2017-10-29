from django.db import models
class Food(models.Model):
    course= models.CharField(max_length = 50)
    cuisine= models.CharField(max_length = 50)
    name= models.CharField(max_length = 50)
    description= models.CharField(max_length = 250)
    price= models.FloatField()
    food_id = models.BigIntegerField(primary_key=True)

# Create your models here.
class Food(models.Model):
	ID=models.BigIntegerField(primary_key=True)
	name=models.CharField(max_length=50)
	description=models.CharField(max_length=300)
	price=models.FloatField()
	course=models.CharField(max_length=50)
	cuisine=models.CharField(max_length=50)
	category=models.CharField(max_length=50)

	def __str__(self):
		return self.name



