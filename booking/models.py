from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField(help_text="Enter number of guests (e.g., 1, 2, 3)")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='room_photos/')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='rooms',
        null=True,
        blank=True
    )
    equipment = models.ManyToManyField(Equipment, blank=True, related_name='rooms')

    is_available = models.BooleanField(default=True, verbose_name="Available for booking")

    def __str__(self):
        return self.name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.room.name}"

class Rating(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.score} for {self.room.name} by {self.user.username}"
