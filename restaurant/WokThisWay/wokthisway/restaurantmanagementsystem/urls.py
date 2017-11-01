from django.conf.urls import url
from . import views

urlpatterns = [

    #localhost/
    url(r'^$', views.index, name= 'index' ),

    #locahost/menu/beverage
    url(r'^beverage/$',views.beverage_menu, name = 'beverage'),
    #locahost/menu/indian_menu
    url(r'^indian_menu/$',views.indian_menu, name = 'indian_menu'),
    #locahost/menu/chinese_menu
    url(r'^chinese_menu/$',views.chinese_menu, name = 'chinese_menu'),
    #locahost/menu/american_menu
    url(r'^american_menu/$',views.american_menu, name = 'american_menu'),
    #locahost/menu/dessert
    url(r'^dessert/$',views.dessert, name = 'dessert'),
]
