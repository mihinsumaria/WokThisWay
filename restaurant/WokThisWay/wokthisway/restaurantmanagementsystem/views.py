from django.shortcuts import render
from .models import Food

# Create your views here.

def index(request):
    return render(request,'restaurantmanagementsystem/index.html',)

def beverage_menu(request):
    food_list = Food.objects.filter(cuisine = 'Beverage')
    return render(request,'restaurantmanagementsystem/food_menu.html',{'food_list':food_list})

def indian_menu(request):
    food_list = Food.objects.filter(cuisine = 'Indian')
    return render(request,'restaurantmanagementsystem/food_menu.html',{'food_list':food_list})

def chinese_menu(request):
    food_list = Food.objects.filter(cuisine = 'Chinese')
    return render(request,'restaurantmanagementsystem/food_menu.html',{'food_list':food_list})

def american_menu(request):
    food_list = Food.objects.filter(cuisine = 'American')
    return render(request,'restaurantmanagementsystem/food_menu.html',{'food_list':food_list})

def dessert(request):
    food_list = Food.objects.filter(cuisine = 'Dessert')
    return render(request,'restaurantmanagementsystem/food_menu.html',{'food_list':food_list})
