from django.shortcuts import render
from .models import Food
from django.db.models import Sum

# Create your views here

class Cart:

    def __init__(self, id,name,qty,price):
        self.id = id
        self.name = name
        self.qty = qty
        self.price = price

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_qty(self):
        return self.qty

    def get_price(self):
        return self.price


# test function gives error while adding all
cart = []


def total_bill():
    global cart
    totalprice =0
    for item in cart:
        totalprice += item.get_price()
    return totalprice


# function Just For Test. Needs to be deleted Later
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

def add_to_cart(request):
    global cart
    foods = request.POST.getlist("food")
    qty = request.POST.getlist("quantity")
    while '' in qty:            # removes unchecked items
        qty.remove('')
    for position,food in enumerate(foods):
        name = Food.objects.values_list('name', flat = True).get(ID = food)
        price = (Food.objects.values_list('price', flat = True).get(ID = food))*float(qty[position])
        cart.append(Cart(food,name,qty[position],price))
    lastItem = cart[len(cart)-1].get_id()
    cuisine = Food.objects.values_list('cuisine', flat = True).get(ID = lastItem)
    food_course = Food.objects.values_list('course', flat = True).get(ID = lastItem)
    food_list = Food.objects.filter(cuisine = cuisine, course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

def cart_transaction(request):
    print("here")
    global cart
    if request.POST:
        # IF THE REMOVE BUTTON PRESSED
        if 'remove' in request.POST:
            print ("remove")
            foods = request.POST.getlist("remove_check")
            print (foods)
            for food in foods:
                print(food)
                for index, item in enumerate(cart) :
                    print(item.get_id())
                    if item.get_id() ==food:
                        print(str(index)+ "index")
                        del cart[index]
            if(len(cart)):
                lastItem = cart[len(cart)-1].get_id()
                cuisine = Food.objects.values_list('cuisine', flat = True).get(ID = lastItem)
                food_course = Food.objects.values_list('course', flat = True).get(ID = lastItem)
                food_list = Food.objects.filter(cuisine = cuisine, course = food_course)
                bill = total_bill()
            else:
                food_list={}
                bill =0
            return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

        #IF ORDER bUTTON PRESSED , TO BE IMPLEMENTED
        elif 'order' in request.POST:
                lastItem = cart[len(cart)-1].get_id()
                cuisine = Food.objects.values_list('cuisine', flat = True).get(ID = lastItem)
                food_course = Food.objects.values_list('course', flat = True).get(ID = lastItem)
                food_list = Food.objects.filter(cuisine = cuisine, course = food_course)
                bill = total_bill()
                return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})



#ONLY FOR TEST. NEEDS TO BE DELETED LATER
def index(request):
    return render(request,'restaurantmanagementsystem/index.html',)

def beverage_menu(request):
    global cart
    food_list = Food.objects.filter(cuisine = 'Beverage')
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

def indian_menu(request,food_course):
    global cart
    food_list = Food.objects.filter(cuisine = 'Indian', course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

def chinese_menu(request,food_course):
    global cart
    food_list = Food.objects.filter(cuisine = 'Chinese', course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

def american_menu(request,food_course):
    global cart
    food_list = Food.objects.filter(cuisine = 'American', course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

def dessert(request):
    global cart
    food_list = Food.objects.filter(cuisine = 'Dessert')
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill})

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
