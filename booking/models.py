from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

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

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.guest_name} - {self.room.name}"
