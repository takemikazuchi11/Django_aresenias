
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
     
    path('admin/', admin.site.urls),
    path('Guest/', include("Guest.urls")),
   path('Admin/', include("Admin.urls")),
  
]
