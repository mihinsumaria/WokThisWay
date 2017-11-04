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
    OrderID = models.IntegerField()
    table_id= models.IntegerField()
    status = models.CharField(max_length = 100)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,)
    food = models.ForeignKey(Food, on_delete=models.PROTECT, )
    timestamp = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField(default=1)
    class Meta:
        unique_together=(('OrderID','food'),)
#Add quantity for relation between food and Order
# timestamp for order
