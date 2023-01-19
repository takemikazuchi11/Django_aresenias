from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student/', include("Student.urls")),
    path('Proffessor/', include("Proffessor.urls")),
    path('Part2/', include("Part2.urls")),
]
