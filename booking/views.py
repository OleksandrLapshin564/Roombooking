from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .models import Category, Room, Booking
from .forms import RegisterForm, BookingForm

def about_view(request):
    return render(request, 'booking/about.html')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'booking/category_list.html', {'categories': categories})

def rooms_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    rooms = category.rooms.all()  # related_name='rooms' from Room model
    return render(request, 'booking/rooms_by_category.html', {
        'category': category,
        'rooms': rooms
    })

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'booking/room_detail.html', {'room': room})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # automatic login after registration
            messages.success(request, "Реєстрація успішна! Вітаємо вас!")
            return redirect("category_list")
    else:
        form = RegisterForm()
    return render(request, "booking/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "booking/login.html"

class CustomLogoutView(LogoutView):
    next_page = "category_list"

@login_required
def book_room_view(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        # We pass room to the instance so that the form can check for uniqueness
        form.instance.room = room
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            # Check for overlapping reservations in the database for this room
            overlapping = Booking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            ).exists()

            if overlapping:
                messages.error(request, "This room is already booked for the selected period.")
            else:
                booking = form.save(commit=False)
                booking.room = room
                booking.user = request.user  # Linking a booking to a user
                booking.save()
                messages.success(request, "Booking successfully created!")
                return redirect("category_list")
    else:
        form = BookingForm()
    return render(request, "booking/book_room.html", {"form": form, "room": room})

@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')  # Showing user's booking
    return render(request, 'booking/my_bookings.html', {'bookings': bookings})
