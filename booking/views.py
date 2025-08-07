from django.shortcuts import render, get_object_or_404
from .models import Category, Room

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
