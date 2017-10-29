from django.db import models
class Food(models.Model):
    course= models.CharField(max_length = 50)
    cuisine= models.CharField(max_length = 50)
    name= models.CharField(max_length = 50)
    description= models.CharField(max_length = 250)
    price= models.FloatField()
    food_id = models.BigIntegerField(primary_key=True)

<<<<<<< HEAD
=======
    def add_dish(self):
        pass
    def remove_dish(self):
        pass
    def get_dishes(self):
        pass
    def modify_price(self):
        pass

>>>>>>> master
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

