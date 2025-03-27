from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Guest, Booking
from .forms import RoomForm, GuestForm, BookingForm

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'inventory/room_list.html', {'rooms': rooms})

def room_add(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'inventory/room_form.html', {'form': form})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'inventory/booking_list.html', {'bookings': bookings})

def home(request):
    return render(request, 'inventory/home.html')