from django.urls import path
from .views import (
    about_view,
    room_detail,
    category_list,
    rooms_by_category,
    register_view,
    CustomLoginView,
    CustomLogoutView,
    book_room_view,
    my_bookings_view,  # import new view
)

urlpatterns = [
    path('', category_list, name='category_list'),  # Home — list of categories
    path('category/<int:category_id>/', rooms_by_category, name='rooms_by_category'),  # Rooms by category
    path('about/', about_view, name='about'),  # About Us Page
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),  # Room details

    # Authentication
    path('register/', register_view, name='register'),  # Registration
    path('login/', CustomLoginView.as_view(), name='login'),  # Login
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout

    # Booking
    path('book/<int:room_id>/', book_room_view, name='book_room'),  # Room reservation

    # My Bookings
    path('my-bookings/', my_bookings_view, name='my_bookings'),  # My bookings page
]
