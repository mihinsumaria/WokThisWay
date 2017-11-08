from django.shortcuts import render
from .models import Food, Order
from django.db.models import Sum

# Create your views here

class Cart:
    def __inti__(self):
        pass

    def __init__(self, id,name,qty,price):
        self.id = id
        self.name = name
        self.qty = qty
        self.price = price

    def get_id(self):
        return self.id

    def set_id(self,id):
        self.id = id
        return

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name
        return

    def get_qty(self):
        return self.qty

    def set_qty(self,qty):
        self.qty = qty
        return

    def get_price(self):
        return self.price

    def set_price(self,price):
        self.price = price
        return

# test function gives error while adding all
cart = []
total=0


def get_index(cart,id):
    for index, item in enumerate(cart):
        if (item.get_id == id):
            print(item.get_id)
            return index


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
        #print(Food.objects.filter(ID = food),qty[position])
        name = Food.objects.values_list('name', flat = True).get(ID = food)
        price = (Food.objects.values_list('price', flat = True).get(ID = food))*float(qty[position])
        cart.append(Cart(food,name,qty[position],price))
    #print("value "+ str(cart[len(cart)-1].get_id()))
    lastItem = cart[len(cart)-1].get_id()
    cuisine = Food.objects.values_list('cuisine', flat = True).get(ID = lastItem)
    food_course = Food.objects.values_list('course', flat = True).get(ID = lastItem)
    food_list = Food.objects.filter(cuisine = cuisine, course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

def cart_transaction(request):
    print("here")
    global cart
    if request.POST:
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
            else:
                food_list={}
            return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

        elif 'order' in request.POST:
                lastItem = cart[len(cart)-1].get_id()
                cuisine = Food.objects.values_list('cuisine', flat = True).get(ID = lastItem)
                food_course = Food.objects.values_list('course', flat = True).get(ID = lastItem)
                food_list = Food.objects.filter(cuisine = cuisine, course = food_course)
                return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})




def index(request):
    return render(request,'restaurantmanagementsystem/index.html',)

def beverage_menu(request):
    global cart
    food_list = Food.objects.filter(cuisine = 'Beverage')
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

def indian_menu(request,food_course):
    global cart
    food_list = Food.objects.filter(cuisine = 'Indian', course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

def chinese_menu(request,food_course):
    global cart
    food_list = Food.objects.filter(cuisine = 'Chinese', course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

def american_menu(request,food_course):
    global cart
    food_list = Food.objects.filter(cuisine = 'American', course = food_course)
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

def dessert(request):
    global cart
    food_list = Food.objects.filter(cuisine = 'Dessert')
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart})

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
