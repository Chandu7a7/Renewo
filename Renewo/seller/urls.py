from django.contrib import admin
from django.urls import path
from seller import views


urlpatterns = [
    
    path("", views.seller , name="seller"),
    path("seller-info", views.sellerinfo , name="seller-info"),
]
