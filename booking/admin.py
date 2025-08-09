from django.contrib import admin
from .models import Room, Booking, Category, Equipment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'price', 'category')
    list_filter = ('capacity', 'category')
    filter_horizontal = ('equipment',)  # додаємо поле для зручного вибору обладнання

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest_name', 'room', 'check_in', 'check_out')
    list_filter = ('check_in', 'check_out')
