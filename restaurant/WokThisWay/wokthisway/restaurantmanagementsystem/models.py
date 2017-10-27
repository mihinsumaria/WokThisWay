from django.db import model
class Food(models.Model):
    course= models.CharField(max_length = 50)
    cuisine= models.CharField(max_length = 50)
    name= models.CharField(max_length = 50)
    description= models.CharField(max_length = 250)
    price= models.FloatField()
    food_id = models.BigIntegerField(primary_key=True)

    def add_dish(self):
        pass
    def remove_dish(self):
        pass
    def get_dishes(self):
        pass
    def modify_price(self):
        pass

# Create your models here.
