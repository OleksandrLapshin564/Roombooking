# booking/serializers.py
from rest_framework import serializers
from .models import Room, Booking, Category, Equipment
from django.contrib.auth.models import User

# --- Category Serializer ---
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# --- Equipment Serializer ---
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


# --- Room Serializer ---
class RoomSerializer(serializers.ModelSerializer):
    # Display category and equipment details in the response
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    equipment = EquipmentSerializer(many=True, read_only=True)
    equipment_ids = serializers.PrimaryKeyRelatedField(
        queryset=Equipment.objects.all(), source='equipment', many=True, write_only=True
    )

    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'description',
            'capacity',
            'price',
            'image',
            'is_available',
            'category',      # full details
            'category_id',   # for create/edit
            'equipment',     # full details
            'equipment_ids', # for create/edit
        ]


# --- Booking Serializer ---
class BookingSerializer(serializers.ModelSerializer):
    # Show full room info in booking responses
    room = RoomSerializer(read_only=True)
    room_id = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source='room', write_only=True
    )
    user = serializers.StringRelatedField(read_only=True)  # show username instead of ID

    class Meta:
        model = Booking
        fields = [
            'id',
            'room',       # full room details
            'room_id',    # for create/edit
            'user',
            'check_in',
            'check_out',
        ]
        read_only_fields = ['user']  # user assigned automatically
