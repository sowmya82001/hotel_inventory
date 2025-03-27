import uuid
from django.db import models

# Hotel Room Model
class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.room_number} - {self.get_room_type_display()}"

# Guest Model
class Guest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

# Booking Model
class Booking(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        num_days = (self.check_out - self.check_in).days
        self.total_price = num_days * self.room.price_per_night
        self.room.is_available = False  # Mark room as occupied
        self.room.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Booking {self.id} - {self.guest.name}"