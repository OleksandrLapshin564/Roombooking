from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from rest_framework import viewsets
from .models import Category, Room, Booking, Equipment
from .forms import RegisterForm, BookingForm
from .serializers import CategorySerializer, RoomSerializer, BookingSerializer, EquipmentSerializer

# --- General Views ---
def about_view(request):
    return render(request, 'booking/about.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'booking/category_list.html', {'categories': categories})


def rooms_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    rooms = category.rooms.all()
    return render(request, 'booking/rooms_by_category.html', {'category': category, 'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    today = timezone.now().date()
    upcoming_bookings = room.booking_set.filter(check_out__gte=today).order_by('check_in')
    return render(request, 'booking/room_detail.html', {'room': room, 'today': today, 'upcoming_bookings': upcoming_bookings})


# --- Authentication Views ---
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome!")
            return redirect("my_bookings")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "booking/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "booking/login.html"


class CustomLogoutView(LogoutView):
    next_page = "category_list"


# --- Booking Views ---
@login_required
def book_room_view(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        booking_instance = Booking(room=room)
        form = BookingForm(request.POST, instance=booking_instance)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            booking.save()
            messages.success(request, "Booking successfully created!")
            return redirect("my_bookings")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        booking_instance = Booking(room=room)
        form = BookingForm(instance=booking_instance)

    return render(request, "booking/book_room.html", {"form": form, "room": room})


@login_required
def my_bookings_view(request):
    today = timezone.now().date()
    bookings = Booking.objects.filter(user=request.user).order_by('-check_in')
    return render(request, 'booking/my_bookings.html', {'bookings': bookings, 'today': today})


# --- DRF API ViewSets ---
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
