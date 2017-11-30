from django.conf.urls import url
from . import views



urlpatterns = [

    #localhost/
    url(r'^$', views.index, name= 'index' ),

    #locahost/menu/beverage
    url(r'^beverage/$',views.beverage_menu, name = 'beverage'),
    #locahost/menu/indian_menu
    url(r'^indian_menu/(?P<food_course>[A-Za-z ]+)$',views.indian_menu, name = 'indian_menu'),
    #locahost/menu/chinese_menu
    url(r'^chinese_menu/(?P<food_course>[A-Za-z ]+)$',views.chinese_menu, name = 'chinese_menu'),
    #locahost/menu/american_menu
    url(r'^american_menu/(?P<food_course>[A-Za-z ]+)$',views.american_menu, name = 'american_menu'),
    #locahost/menu/dessert
    url(r'^dessert/$',views.dessert, name = 'dessert'),
    #locahost/login_page
    url(r'^login_page/$',views.login_page, name = 'login_page'),
    #Customer's Menu
    url(r'^login_page/menu/$',views.menu_page, name = 'menu_page'),
    #Guest's Menu
    url(r'^menu/$',views.guest_menu_page, name = 'guest_menu_page'),

    url(r'^register/$',views.register, name = 'register'),

    url(r'^orderStart/$',views.add_to_cart, name = 'add_to_cart'),

    url(r'^orderTrans/$',views.cart_transaction, name = 'cart_transaction'),

########################################
    url(r'^cashier/$',views.cashier, name = 'cashier'),
    url(r'^cashier_login_page/$',views.cashier_login_page, name = 'cashier_login_page'),
    url(r'^cashierlogout/$',views.cashierlogout, name = 'cashierlogout'),
    url(r'^cTrans/$',views.cashier_transaction, name = 'cashier_transaction'),
##########################################################
    url(r'^manager/$',views.manager, name = 'manager'),
    url(r'^newDish/$',views.add_dish, name = 'add_dish'),
    url(r'^delDish/$',views.del_dish, name = 'del_dish'),
    url(r'^add_emp/$',views.add_emp, name = 'add_emp'),
    url(r'^del_emp/$', views.del_emp, name='del_emp'),
#########################################################
    url(r'^logout/$',views.logout, name = 'logout'),
    
]
