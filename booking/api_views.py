# booking/api_views.py
from rest_framework import viewsets, permissions
from .models import Room, Booking, Category, Equipment
from .serializers import RoomSerializer, BookingSerializer, CategorySerializer, EquipmentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# --- Category API ---
class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for viewing and managing categories."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]  # Guests can view, only authenticated can create/edit

# --- Equipment API ---
class EquipmentViewSet(viewsets.ModelViewSet):
    """API endpoint for viewing and managing equipment."""
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [AllowAny]  # Guests can view, only authenticated can create/edit

# --- Room API ---
class RoomViewSet(viewsets.ModelViewSet):
    """API endpoint for viewing, creating, editing, and deleting rooms."""
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]  # Guests can view, only authenticated can create/edit

# --- Booking API ---
class BookingViewSet(viewsets.ModelViewSet):
    """API endpoint for working with reservations."""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Only authorized users can view/create

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the booking
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Users see only their own bookings
        return Booking.objects.filter(user=self.request.user)
