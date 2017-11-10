from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum
from .forms import *

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
def add_to_cart(request):
    username=request.session['username']
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
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})

def cart_transaction(request):
    username=request.session['username']
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
                return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})



#ONLY FOR TEST. NEEDS TO BE DELETED LATER
def index(request):
    if(request.session.has_key('username')):
        return redirect(guest_menu_page)
    return render(request,'restaurantmanagementsystem/index.html',)

def beverage_menu(request):
    username=request.session['username']
    global cart
    food_list = Food.objects.filter(cuisine = 'Beverage')
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})

def indian_menu(request,food_course):
    username=request.session['username']
    global cart
    food_list = Food.objects.filter(cuisine = 'Indian', course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})

def chinese_menu(request,food_course):
    username=request.session['username']
    global cart
    food_list = Food.objects.filter(cuisine = 'Chinese', course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})

def american_menu(request,food_course):
    username=request.session['username']
    global cart
    food_list = Food.objects.filter(cuisine = 'American', course = food_course)
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})

def dessert(request):
    username=request.session['username']
    global cart
    food_list = Food.objects.filter(cuisine = 'Dessert')
    bill = total_bill()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username})

def login_page(request,loggedin=0):
    loggedin=0
    pwd=""
    dbpwd=""
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get("name","")
            password=request.POST.get("password","")
            if(Customer.objects.filter(name=username)):
                if(password==Customer.objects.filter(name=username).values('password')[0]['password']):
                    request.session['username']=username
                    food_list=[]
                    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'username':username})
                else:
                    loggedin=1
            else:
                loggedin=1
            return render(request,'restaurantmanagementsystem/login_page.html',{'form':form,'loggedin':loggedin})
    else:
        if(request.session.has_key('username')):
            food_list=[]
            return redirect(guest_menu_page)
        form=LoginForm()
    return render(request,'restaurantmanagementsystem/login_page.html',{'form':form,'loggedin':loggedin})

def logout(request):
    del request.session['username']
    return redirect(index)
def menu_page(request):
    return render(request,'restaurantmanagementsystem/menu.html')
    

def guest_menu_page(request):
    if(request.session.has_key('username')):
        food_list=[]
        username=request.session['username']
        return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'username':username})
    else:
        return redirect(login_page)

def register(request,registered=0):
    if(request.session.has_key('username')):
        return redirect(guest_menu_page)
    fpassword=""
    fcpassword=""
    if(request.method=="POST"):
        form=RegisterForm(request.POST)
        fpassword=request.POST.get("password","")
        fcpassword=request.POST.get("confirmpassword","")
        if form.is_valid():
            if(fpassword==fcpassword and not Customer.objects.filter(name=request.POST.get("name",""))):
                registered=1
                customer=form.save(commit=False)
                customer.save()
            elif(Customer.objects.filter(name=request.POST.get("name",""))):
                registered=3
            elif(fpassword!=fcpassword):
                registered=2
            
            
        return render(request,'restaurantmanagementsystem/registration.html',{'form':form,'registered':registered})

    else:
        form = RegisterForm()
        return render(request,'restaurantmanagementsystem/registration.html',{'form':form,'registered':registered})
