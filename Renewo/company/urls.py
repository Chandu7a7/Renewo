from django.contrib import admin
from django.urls import path
from company import views


urlpatterns = [
    
    path("", views.companys , name="companys"),
    path("company-info",views.companyinfo, name='companyinfo')
]
