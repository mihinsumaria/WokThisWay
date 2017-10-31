from django.db import models
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

class Customer(models.Model):
    ID =  models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Cashier(models.Model):
    ID =  models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Manager(models.Model):
    ID =  models.BigIntegerField(primary_key=True)
    name= models.CharField(max_length=50)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Order(models.Model):
    ID = models.AutoField(primary_key = True)
    table_id= models.IntegerField()
    status = models.CharField(max_length = 100)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,)
    food = models.ManyToManyField(Food, verbose_name="Food items", )
