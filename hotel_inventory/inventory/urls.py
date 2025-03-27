from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.room_add, name='room_add'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('bookings/', views.booking_list, name='booking_list'),
]
