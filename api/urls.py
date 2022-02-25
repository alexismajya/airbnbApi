from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAccommodate),
    path('add/', views.addAccommodate),
    path('rooms', views.getRoom),
    path('addRoom', views.addRoom),
]