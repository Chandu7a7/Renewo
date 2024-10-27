from django.contrib import admin
from django.urls import path
from home import views
from . import *


urlpatterns = [
    path("", views.index , name="home"),
    path("signup/", views.signup , name="signup"),
    path("signin/", views.signin , name="signin"),
    
    path("cart/", views.cart , name="cart"),
    path("cart/add", views.add_to_cart , name="add_to_cart"),
    path("search/", views.search , name="search"),
   
  
]
