# booking/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (
    about_view,
    room_detail,
    category_list,
    rooms_by_category,
    register_view,
    CustomLoginView,
    CustomLogoutView,
    book_room_view,
    my_bookings_view,
)
from .api_views import RoomViewSet, BookingViewSet, CategoryViewSet, EquipmentViewSet

# --- DRF Router ---
router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'bookings', BookingViewSet, basename='booking')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'equipments', EquipmentViewSet, basename='equipment')

# --- URL Patterns ---
urlpatterns = [
    # Frontend pages
    path('', category_list, name='category_list'),
    path('category/<int:category_id>/', rooms_by_category, name='rooms_by_category'),
    path('about/', about_view, name='about'),
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),

    # Authentication
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Booking
    path('book/<int:room_id>/', book_room_view, name='book_room'),
    path('my-bookings/', my_bookings_view, name='my_bookings'),

    # DRF API
    path('api/', include(router.urls)),               # API endpoints for rooms, bookings, categories, equipments
    path('api-auth/', include('rest_framework.urls')),  # Browsable API login/logout
]
