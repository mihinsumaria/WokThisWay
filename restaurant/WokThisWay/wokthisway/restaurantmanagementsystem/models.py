from django.db import models
from django.utils import timezone
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
    #ID =  models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Cashier(models.Model):
    #ID =  models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Manager(models.Model):
    #ID =  models.BigIntegerField(primary_key=True)
    name= models.CharField(max_length=50)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Order(models.Model):
	OrderID = models.IntegerField()
	table_id= models.IntegerField()
	status = models.CharField(max_length = 100)
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT,)
	food = models.ForeignKey(Food, on_delete=models.PROTECT, )
	timestamp = models.DateTimeField(default=timezone.now)
	quantity = models.IntegerField(default=1)
	def __str__(self):
		return str(self.OrderID)+" "+ str(self.customer)+ " "+ str(self.food)
	class Meta:
		unique_together=(('OrderID','food'),)

class Table(models.Model):
	table_id = models.IntegerField(primary_key = True)
	status = models.IntegerField()

	def __str__(self):
		return str(self.table_id)
