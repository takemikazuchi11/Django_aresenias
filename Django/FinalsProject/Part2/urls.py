#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index),
    path('welcome2/',views.welcome2,name="welcome2"),
    path('goForm2/',views.goForm2,name="goForm2"),
    path('goTable2', views.goTable2,name="goTable2"),
    
]