from django.conf.urls import url
from . import views

urlpatterns = [

    #localhost/
    url(r'^$', views.index, name= 'index' ),

    #locahost/menu/beverage
    url(r'^beverage/$',views.beverage_menu, name = 'beverage'),
    #locahost/menu/indian_food
    url(r'^indian_menu/$',views.indian_menu, name = 'indian_menu'),
]
