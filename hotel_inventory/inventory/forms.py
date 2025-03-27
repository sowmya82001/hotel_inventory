from django import forms
from .models import Room, Guest, Booking

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price_per_night', 'is_available']

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'room', 'check_in', 'check_out']
