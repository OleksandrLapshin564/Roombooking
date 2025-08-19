from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Room"
        verbose_name_plural = "Rooms"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.room.name}"

    class Meta:
        ordering = ["date_from"]
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
