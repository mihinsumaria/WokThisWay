from django.contrib import admin
from .models import Food, Cashier, Manager, Customer, Order

admin.site.register(Food)
admin.site.register(Cashier)
admin.site.register(Manager)
admin.site.register(Order)
admin.site.register(Customer)


# Register your models here.
