from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Room, Booking, Rating
from .forms import BookingForm, RatingForm, UserRegistrationForm


# ---------------------------
# Room views
# ---------------------------

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    ratings = Rating.objects.filter(room=room).order_by('-created_at')

    bookings_form = BookingForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        # Booking processing
        if 'booking_submit' in request.POST:
            bookings_form = BookingForm(request.POST)
            if bookings_form.is_valid():
                booking = bookings_form.save(commit=False)
                booking.room = room
                booking.user = request.user if request.user.is_authenticated else None
                if booking.date_from < timezone.now().date():
                    messages.error(request, "Start date cannot be in the past.")
                elif booking.date_to <= booking.date_from:
                    messages.error(request, "End date must be after start date.")
                else:
                    booking.save()
                    messages.success(request, "Room successfully reserved!")
                    return redirect('room_detail', room_id=room.id)
            else:
                messages.error(request, "Please correct the errors in the booking form.")

        # Rating processing
        elif 'rating_submit' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.room = room
                rating.user = request.user if request.user.is_authenticated else None
                rating.save()
                messages.success(request, "Thank you for your feedback!")
                return redirect('room_detail', room_id=room.id)
            else:
                messages.error(request, "Please correct the errors in the rating form.")

    context = {
        'room': room,
        'bookings_form': bookings_form,
        'rating_form': rating_form,
        'ratings': ratings,
    }
    return render(request, 'booking/room_detail.html', context)


# ---------------------------
# Static pages
# ---------------------------

def about(request):
    return render(request, 'booking/about.html')


# ---------------------------
# Categories
# ---------------------------

def category_list(request):
    categories = ['single', 'double', 'lux']  # приклад категорій
    return render(request, 'booking/category_list.html', {'categories': categories})


def rooms_by_category(request, room_type):
    rooms = Room.objects.filter(room_type=room_type)
    return render(request, 'booking/rooms_by_category.html', {'rooms': rooms, 'room_type': room_type})


# ---------------------------
# User registration
# ---------------------------

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'booking/register.html', {'form': form})
