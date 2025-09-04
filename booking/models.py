from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ]

    name = models.CharField(max_length=100)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES, default='single')
    description = models.TextField(blank=True, null=True)
    equipment = models.ManyToManyField(Equipment, blank=True)  # 🔹 зв'язок з Equipment
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()})"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # null для старих записів
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking: {self.user.username if self.user else 'Unknown'} -> {self.room.name}"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()  # 1-5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Rating: {self.user.username} -> {self.room.name}: {self.score}"
