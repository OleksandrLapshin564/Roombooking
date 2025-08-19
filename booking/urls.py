from django.urls import path, include
from .views import about_view, room_list, room_detail

urlpatterns = [
    # HTML routes
    path('', room_list, name='room_list'),  # home page
    path('about/', about_view, name='about'),  # "About us" page
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),  # room details

    # REST API routes
    path('api/', include('booking.api.urls')),  # all routes from the api folder
]
