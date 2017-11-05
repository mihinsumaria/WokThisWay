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
]
