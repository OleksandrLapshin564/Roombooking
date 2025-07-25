from django.http import HttpResponse
from django.shortcuts import render

# Static room data — now with description
ROOMS = [
    {"id": 1, "name": "Room 101", "capacity": 6, "description": "Perfect for small meetings."},
    {"id": 2, "name": "Room 102", "capacity": 10, "description": "Great for workshops."},
    {"id": 3, "name": "Room 201", "capacity": 8, "description": "Spacious and bright."},
]

def about_view(request):
    return render(request, 'booking/about.html')

def room_list(request):
    return render(request, 'booking/room_list.html', {'rooms': ROOMS})

def room_detail(request, room_id):
    room = next((room for room in ROOMS if room['id'] == room_id), None)
    if room is None:
        return HttpResponse("Room not found", status=404)
    return render(request, 'booking/room_detail.html', {'room': room})
