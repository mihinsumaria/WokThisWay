from django.shortcuts import render,redirect
from django.db.models import Max,Count
from .models import *
from django.db.models import Sum
from .forms import *
import datetime
import collections
import pandas as pd
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import os
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here

class Cart:

    def __init__(self, id,name,qty,price,tableId):
        self.id = id
        self.name = name
        self.qty = qty
        self.price = price
        self.tableId=tableId


    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_qty(self):
        return self.qty

    def get_price(self):
        return self.price

    def get_tableId(self):
        return self.tableId


# test function gives error while adding all
cart = []



def get_order_id():
    if(Order.objects.all().aggregate(Count('OrderID'))['OrderID__count']!=0):
        OrderID= Order.objects.all().aggregate(Max('OrderID'))['OrderID__max']
        print(Order.objects.all().aggregate(Count('OrderID'))['OrderID__count'])
    else:
        OrderID=0
    return OrderID

def total_bill():
    global cart
    totalprice =0
    for item in cart:
        totalprice += item.get_price()
    return "{0:.2f}".format(totalprice)



def add_to_cart(request):
    username=request.session['username']
    global cart
    foods = request.POST.getlist("food")
    qty = request.POST.getlist("quantity")
    #tableId = request.POST.get("tableId")
    tableId=request.session['tableid']
    print(tableId)
    while '' in qty:            # removes unchecked items
        qty.remove('')
    for position,food in enumerate(foods):
        name = Food.objects.values_list('name', flat = True).get(ID = food)
        price = (Food.objects.values_list('price', flat = True).get(ID = food))*float(qty[position])
        cart.append(Cart(food,name,qty[position],price,tableId))
    lastItem = cart[len(cart)-1].get_id()
    cuisine = Food.objects.values_list('cuisine', flat = True).get(ID = lastItem)
    food_course = Food.objects.values_list('course', flat = True).get(ID = lastItem)
    food_list = Food.objects.filter(cuisine = cuisine, course = food_course)
    bill = total_bill()
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation})

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
            recommendation = get_recommedations()
            return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation})

        #IF ORDER bUTTON PRESSED
        elif 'order' in request.POST:

                current_orderID = get_order_id() + 1
                currentTable = cart[0].get_tableId()
                table = Table.objects.get(table_id = currentTable)
                table.status=1   # table status 0 - Unoccupied 1- Occupied
                table.save()
                for item in cart:
                    order =Order()
                    order.OrderID = current_orderID
                    order.table_id = item.get_tableId()
                    order.status = 0
                    currentCustomer = Customer.objects.get(name = username)       # 0 - Order Pending 1- Order Done
                    order.customer = currentCustomer
                    currentFood = Food.objects.get(ID = item.get_id())
                    order.food = currentFood
                    order.quantity = item.get_qty()
                    order.save()
                cart.clear()
                return render(request,'restaurantmanagementsystem/test.html',)


#ONLY FOR TEST. NEEDS TO BE DELETED LATER
def index(request):
    if(request.session.has_key('username')):
        return redirect(guest_menu_page)
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/index.html',{'recommendation':recommendation})


def beverage_menu(request):
    username=request.session['username']
    tableid=request.session['tableid']
    global cart
    food_list = Food.objects.filter(cuisine = 'Beverage')
    bill = total_bill()
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation,'tableid':tableid})

def indian_menu(request,food_course):
    username=request.session['username']
    tableid=request.session['tableid']
    global cart
    food_list = Food.objects.filter(cuisine = 'Indian', course = food_course)
    bill = total_bill()
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation,'tableid':tableid})

def chinese_menu(request,food_course):
    username=request.session['username']
    tableid=request.session['tableid']
    global cart
    food_list = Food.objects.filter(cuisine = 'Chinese', course = food_course)
    bill = total_bill()
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation,'tableid':tableid})

def american_menu(request,food_course):
    username=request.session['username']
    tableid=request.session['tableid']
    global cart
    food_list = Food.objects.filter(cuisine = 'American', course = food_course)
    bill = total_bill()
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation,'tableid':tableid})

def dessert(request):
    username=request.session['username']
    tableid=request.session['tableid']
    global cart
    food_list = Food.objects.filter(cuisine = 'Dessert')
    bill = total_bill()
    recommendation = get_recommedations()
    return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'cart':cart,'bill':bill,'username':username,'recommendation':recommendation,'tableid':tableid})

def login_page(request,loggedin=0):
    loggedin=0
    pwd=""
    dbpwd=""
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get("name","")
            password=request.POST.get("password","")
            tableid=request.POST.get("tableID","")
            table=Table.objects.get(table_id=tableid)
            if(Customer.objects.filter(name=username)):
                if(password==Customer.objects.filter(name=username).values('password')[0]['password'] and table.status==0):
                    request.session['username']=username
                    request.session['tableid']=tableid
                    food_list=[]
                    table.status=1
                    table.save()
                    render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'username':username,'tableid':tableid})
                    return redirect(guest_menu_page)
                else:
                    if(table.status==1):
                        loggedin=2
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
    tableid=request.session['tableid']
    table=Table.objects.get(table_id=tableid)
    table.status=0
    table.save()
    customer = Customer.objects.get(name =request.session['username'] )
    orders = Order.objects.filter(customer = customer, table_id= tableid, status = 0)
    if(orders != None):
        for order in orders:
            order.status =2
            order.save()


    del request.session['username']
    return redirect(index)
def menu_page(request):
    return render(request,'restaurantmanagementsystem/menu.html')


def guest_menu_page(request):
    if(request.session.has_key('username')):
        global cart
        food_list = Food.objects.all()
        bill = total_bill()
        recommendation = get_recommedations()
        username=request.session['username']
        tableid=request.session['tableid']
        #print(recommendation)
        return render(request,'restaurantmanagementsystem/menu.html',{'food_list':food_list,'username':username,'tableid':tableid,'recommendation':recommendation,'bill':bill})
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

####################### CASHIER FUNCTIONS #################################
def cashier(request):
    if(request.session.has_key('cashierusername')):
        orders = Order.objects.filter(status= 0)
        tables =  Table.objects.all()
        return render(request,'restaurantmanagementsystem/cashier.html',{'tables':tables,'orders':orders})
    else:
        return redirect(cashier_login_page)
def cashier_transaction(request):
    if request.POST:
        # IF THE REMOVE BUTTON PRESSED
        if 'remove' in request.POST:
            print ("remove")
            done_orders = request.POST.getlist("remove_check")
            for item in done_orders:
                current_order = item.split(":")
                food = Food.objects.get(name = current_order[0])
                order = Order.objects.get(food = food,table_id = current_order[1], status = 0)
                order.status=1
                order.save()
    orders = Order.objects.filter(status= 0)
    tables =  Table.objects.all()
    render(request,'restaurantmanagementsystem/cashier.html',{'tables':tables,'orders':orders})
    return redirect(cashier)

def cashier_login_page(request,loggedin=0):
    loggedin=0
    pwd=""
    dbpwd=""
    if request.method=='POST':
        form=CashierLoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get("name","")
            password=request.POST.get("password","")

            if(Cashier.objects.filter(name=username)):
                cash=Cashier.objects.get(name=username)
                if(password==cash.password):
                    request.session['cashierusername']=username
                    print(request.session['cashierusername'])
                    orders = Order.objects.filter(status= 0)
                    tables =  Table.objects.all()
                    render(request,'restaurantmanagementsystem/cashier.html',{'tables':tables,'orders':orders})
                    return redirect(cashier)
                else:
                    loggedin=1
            else:
                loggedin=1
            return render(request,'restaurantmanagementsystem/cashier_login_page.html',{'form':form,'loggedin':loggedin})
    else:
        if(request.session.has_key('cashierusername')):
            return redirect(cashier)
        form=CashierLoginForm()
    return render(request,'restaurantmanagementsystem/cashier_login_page.html',{'form':form,'loggedin':loggedin})

def cashierlogout(request):
    del request.session['cashierusername']
    return redirect(cashier_login_page)



    ####################### MANAGER FUNCTIONS #################################


def manager(request):
    if(request.session.has_key('managerusername')):
        table = calcSeven()
        saleoftheday=graphing(table)
        return render(request,'restaurantmanagementsystem/manager.html',{'table':table,'saleoftheday':saleoftheday})
    else:
        return redirect(manager_login_page)


def manager_login_page(request,loggedin=0):
    loggedin=0
    #pwd=""
    #dbpwd=""
    if request.method=='POST':
        form=ManagerLoginForm(request.POST)
        if form.is_valid():
            username=request.POST.get("name","")
            password=request.POST.get("password","")
            user=authenticate(username=username,password=password)
            if(user):
                request.session['managerusername']=username
                table = calcSeven()
                saleoftheday=graphing(table)
                render(request,'restaurantmanagementsystem/manager.html',{'table':table,'saleoftheday':saleoftheday})
                return redirect(manager)
            else:
                loggedin=1
        else:
            loggedin=1
        return render(request,'restaurantmanagementsystem/manager_login_page.html',{'form':form,'loggedin':loggedin})
    else:
        if(request.session.has_key('managerusername')):
            return redirect(manager)
        form=ManagerLoginForm()
    return render(request,'restaurantmanagementsystem/manager_login_page.html',{'form':form,'loggedin':loggedin})

def managerlogout(request):
    del request.session['managerusername']
    return redirect(manager_login_page)

def add_dish(request):
    food_id = request.POST.get("id")
    name =request.POST.get("name")
    description =request.POST.get("description")
    cuisine = request.POST.get("cuisine")
    category= request.POST.get("category")
    price = request.POST.get("price")
    course = request.POST.get("course")
    food = Food(ID = food_id,name = name,description = description, cuisine = cuisine,category = category, price = price,course =course)
    food.save()
    table = calcSeven()
    saleoftheday=graphing(table)
    render(request,'restaurantmanagementsystem/manager.html',{'table':table,'saleoftheday':saleoftheday})
    return redirect(manager)

def del_dish(request):

    name =request.POST.get("name")
    food = Food.objects.get(name = name)
    food.delete()
    table = calcSeven()
    return render(request,'restaurantmanagementsystem/manager.html',{'table':table})

def add_emp(request):
    name = request.POST.get("name")
    password = request.POST.get("password")
    cashier = Cashier(name=name, password=password)
    cashier.save()
    table = calcSeven()
    saleoftheday=graphing(table)
    render(request,'restaurantmanagementsystem/manager.html',{'table':table,'saleoftheday':saleoftheday})
    return redirect(manager)


def del_emp(request):
    name = request.POST.get("name")
    password = request.POST.get("password")
    cashier1 = Cashier.objects.get(name=name, password=password)
    cashier1.delete()
    table = calcSeven()
    saleoftheday=graphing(table)
    render(request,'restaurantmanagementsystem/manager.html',{'table':table,'saleoftheday':saleoftheday})
    return redirect(manager)

def calcSeven():
    orders= Order.objects.filter(status=1)
    table = dict()
    for i in range(0,7):
        dd= datetime.datetime.now() - datetime.timedelta(days=i)
        table[dd.date()] = 0
    for order in orders:

        key = order.timestamp.date()
        a =(order.food.price * order.quantity)
        print(key,a)
        if( key in table):
            food = Food.objects.get(name = order.food)
            a =(order.food.price * order.quantity)
            print("a" + str(a))
            table[key] = table[key] + a
    sorted_table = collections.OrderedDict(sorted(table.items()))
    return sorted_table

def graphing(sorted_table):
    df=pd.DataFrame(sorted_table,index=[0])
    x=[str(i) for i in df]
    y=[df[i][0] for i in df]
    fig,ax=plt.subplots()
    ax.bar(x,y,color='#f4511e')
    for label in ax.get_xticklabels():
        label.set_rotation(25)
    rects=ax.patches
    labels=[str(i) for i in y]
    for rect, label in zip(rects,labels):
        height=rect.get_height()
        if(height==0):
            ax.text(rect.get_x()+rect.get_width()/2,height+5,label,ha='center',va='bottom')
        else:
            ax.text(rect.get_x()+rect.get_width()/2,height-5,label,ha='center',va='bottom')
    saleoftheday=y[-1]
    path=os.path.join(os.path.dirname(__file__),'static/images/')+'analytics.png'
    plt.savefig(path)
    return saleoftheday

def get_recommedations():
    recommendation=dict()
    foodFreq = Order.objects.values_list('food').annotate(Count('food'))
    for food,freq in foodFreq:
        name = Food.objects.values_list('name', flat = 'True').get(ID= food)
        recommendation[name]= freq
    recommendationSorted =sorted(recommendation.items(), key=lambda x: x[1])
    lenght = len(recommendationSorted)
    if(lenght>4):
        recommendationSorted = recommendationSorted[lenght-4:lenght]
    return reversed(recommendationSorted)
