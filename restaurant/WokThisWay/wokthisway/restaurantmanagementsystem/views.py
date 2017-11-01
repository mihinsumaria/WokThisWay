from django.shortcuts import render
from .models import Food

# Create your views here.

def index(request):
    return render(request,'restaurantmanagementsystem/index.html',)

def beverage_menu(request):
    beverage_list = Food.objects.filter(cuisine = 'Beverage')
    return render(request,'restaurantmanagementsystem/beverage.html',{'beverage_list':beverage_list})

def indian_menu(request):
    indain_food_list = Food.objects.filter(cuisine = 'Indian')
    return render(request,'restaurantmanagementsystem/indian_food.html',{'indain_food_list':indain_food_list})
