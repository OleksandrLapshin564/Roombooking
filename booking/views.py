from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Room, Booking, Rating
from .forms import BookingForm, RatingForm, UserRegistrationForm

import os
import openai
from openai import RateLimitError, AuthenticationError

# -----------------------------
# OpenAI setup
# -----------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(prompt: str, model: str = "gpt-5-mini"):
    """
    Makes a request to OpenAI and returns a text response.
    If there is no balance or an error occurs, returns a mock response.
    """
    try:
        response = openai.responses.create(
            model=model,
            input=prompt
        )
        return response.output_text
    except (RateLimitError, AuthenticationError):
        return f"[Mock response for '{prompt}' with model '{model}']"
    except Exception as e:
        return f"An unknown error occurred: {e}"


# ---------------------------
# Room views
# ---------------------------

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    ratings = Rating.objects.filter(room=room).order_by('-created_at')

    booking_form = BookingForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        if 'booking_submit' in request.POST:
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.room = room
                booking.user = request.user if request.user.is_authenticated else None

                if booking.check_in < timezone.now().date():
                    messages.error(request, "Start date cannot be in the past.")
                elif booking.check_out <= booking.check_in:
                    messages.error(request, "End date must be after start date.")
                else:
                    booking.save()
                    messages.success(request, "Room successfully reserved!")
                    return redirect('booking:room_detail', room_id=room.id)
            else:
                messages.error(request, "Please correct the errors in the booking form.")

        elif 'rating_submit' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating = rating_form.save(commit=False)
                rating.room = room
                rating.user = request.user if request.user.is_authenticated else None
                rating.save()
                messages.success(request, "Thank you for your feedback!")
                return redirect('booking:room_detail', room_id=room.id)
            else:
                messages.error(request, "Please correct the errors in the rating form.")

    context = {
        'room': room,
        'booking_form': booking_form,
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
    categories = [
        {'slug': 'single', 'name': 'Single'},
        {'slug': 'double', 'name': 'Double'},
        {'slug': 'suite', 'name': 'Suite'},
    ]
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
            return redirect('booking:login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserRegistrationForm()
    return render(request, 'booking/register.html', {'form': form})


# ---------------------------
# OpenAI test view
# ---------------------------

def openai_test(request):
    """
    Simple view to test OpenAI responses.
    Accepts GET or POST with 'prompt'.
    """
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        result = get_openai_response(prompt)
        return render(request, "booking/openai_test.html", {"prompt": prompt, "response_text": result})
    else:
        prompt = request.GET.get("prompt", "Write a short bedtime story about a unicorn.")
        return render(request, "booking/openai_test.html", {"prompt": prompt})
