from django.shortcuts import render
from .models import Food
from django.db.models import Sum

# Create your views here

def test(request):
    foods = request.POST.getlist("food")
    price =[]
    i=0
    for id in foods:
         price[i,1] = Food.objects.filter(ID = id).values('price')
         i = i+1
    print(price)
    qty = request.POST.getlist("quantity")
    while '' in qty:
        qty.remove('')
    return render(request,'restaurantmanagementsystem/test.html',{'foods':foods, 'qty': qty})


def index(request):
    return render(request,'restaurantmanagementsystem/index.html',)

def beverage_menu(request):
    food_list = Food.objects.filter(cuisine = 'Beverage')
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list})

def indian_menu(request,food_course):
    food_list = Food.objects.filter(cuisine = 'Indian', course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list})

def chinese_menu(request,food_course):
    food_list = Food.objects.filter(cuisine = 'Chinese', course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list})

def american_menu(request,food_course):
    food_list = Food.objects.filter(cuisine = 'American', course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list})

def dessert(request):
    food_list = Food.objects.filter(cuisine = 'Dessert')
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list})

def login_page(request):
    return render(request,'restaurantmanagementsystem/login_page.html')

def menu_page(request):
    username = request.POST.get('username')
    if(username == 'vaseem'):
        return render(request,'restaurantmanagementsystem/menu.html')
    return render(request,'restaurantmanagementsystem/test.html')

def guest_menu_page(request):
    food_list=[]
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list})

def register(request):
    return render(request,'restaurantmanagementsystem/registration.html')
