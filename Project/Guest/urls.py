#from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index),
    path('ghome',views.gHome,name="gHome"),
    path('gLogin',views.gLogin,name="gLogin"),
    path('gRegister',views.gRegister,name="gRegister"),
    path('gAbout',views.gAbout,name="gAbout"),
    path('gService',views.gService,name="gService"),
    path('gService',views.gService,name="gService"),
     path('gHPage',views.gHPAge,name="gHPage"),
     path('gBook',views.gBook,name="gBook"),
    
    
]