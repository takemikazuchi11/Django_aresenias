#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index),
    path('pwelcome/',views.pwelcome,name="pwelcome"),
    path('pgoForm/',views.pgoForm,name="pgoForm"),
    path('pgoTable/', views.pgoTable,name="pgoTable"),
    
]