from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.start, name='start'),
    path('home/',views.home),
    path('aHome',views.aHome,name="aHome"),

    # Function for User List
    path('aUser',views.aUser,name="aUser"),
    path('aPackages',views.aPackages,name="aPackages"),
    path('aAppointment',views.aAppointment,name="aAppointment"),
    path('aUUpdate/<int:id>',views.aUUpdate,name="aUUpdate"),
    path('aUEdit/<int:id>',views.aUEdit,name="aUEdit"),
    path('aUDelete/<int:id>',views.aUDelete,name="aUDelete"),

    # Function for Package Services List
    path('aPAdd',views.aPAdd,name="aPAdd"),
    path('aPUpdate/<int:id>',views.aPUpdate,name="aPUpdate"),
    path('aPEdit/<int:id>',views.aPEdit,name="aPEdit"),
    path('aPDelete/<int:id>',views.aPDelete,name="aPDelete"),

     # Function for BookForm List
    path('aBookForm',views.aBookForm,name="aBookForm"),
     path('aBDelete/<int:id>',views.aBDelete,name="aBDelete"),
    
]