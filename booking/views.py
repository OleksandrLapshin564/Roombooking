from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Room, Booking, Rating
from .forms import BookingForm, RatingForm


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    # Отримуємо всі відгуки
    ratings = Rating.objects.filter(room=room).order_by('-created_at')

    # Створюємо порожні форми
    bookings_form = BookingForm()
    rating_form = RatingForm()

    # Якщо є POST-запит
    if request.method == 'POST':
        # Обробка бронювання
        if 'booking_submit' in request.POST:
            bookings_form = BookingForm(request.POST)
            if bookings_form.is_valid():
                booking = bookings_form.save(commit=False)
                booking.room = room
                booking.user = request.user if request.user.is_authenticated else None
                # Перевірка дат
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

        # Обробка рейтингу
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
