#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index),
    path('welcome/',views.welcome,name="welcome"),
    path('goForm/',views.goForm,name="goForm"),
    path('goTable', views.goTable,name="goTable"),
    
]