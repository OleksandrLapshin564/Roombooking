# booking/management/commands/populate_rooms.py

from django.core.management.base import BaseCommand
from booking.models import Room

class Command(BaseCommand):
    help = 'Populate the database with initial rooms'

    def handle(self, *args, **kwargs):
        # Room categories
        categories = {
            'Single': [
                {'name': 'Single Cozy', 'price': 50, 'capacity': 1, 'equipment': 'Bed, Desk, Chair', 'image': 'rooms/sng_600_001.jpg'},
                {'name': 'Single Modern', 'price': 55, 'capacity': 1, 'equipment': 'Bed, Desk, Chair, TV', 'image': 'rooms/sng_600_002.jpg'},
                {'name': 'Single Classic', 'price': 60, 'capacity': 1, 'equipment': 'Bed, Wardrobe, Desk', 'image': 'rooms/sng_600_003.jpg'},
                {'name': 'Single Compact', 'price': 48, 'capacity': 1, 'equipment': 'Bed, Chair', 'image': 'rooms/sng_600_004.jpg'},
                {'name': 'Single Deluxe', 'price': 70, 'capacity': 1, 'equipment': 'Bed, Desk, Chair, TV, Mini-fridge', 'image': 'rooms/sng_600_005.jpg'},
            ],
            'Double': [
                {'name': 'Double Cozy', 'price': 80, 'capacity': 2, 'equipment': '2 Beds, Desk, Chair', 'image': 'rooms/db1_600_001.webp'},
                {'name': 'Double Modern', 'price': 85, 'capacity': 2, 'equipment': '2 Beds, Desk, Chair, TV', 'image': 'rooms/db2_600_002.jpg'},
                {'name': 'Double Classic', 'price': 90, 'capacity': 2, 'equipment': '2 Beds, Wardrobe, Desk', 'image': 'rooms/db3_600_003.jpg'},
                {'name': 'Double Compact', 'price': 78, 'capacity': 2, 'equipment': '2 Beds, Chair', 'image': 'rooms/db4_600_004.webp'},
                {'name': 'Double Deluxe', 'price': 100, 'capacity': 2, 'equipment': '2 Beds, Desk, Chair, TV, Mini-fridge', 'image': 'rooms/db5_600_005.webp'},
            ],
            'Luxury': [
                {'name': 'Luxury Suite 1', 'price': 150, 'capacity': 3, 'equipment': 'King Bed, Sofa, Desk, TV, Mini-fridge', 'image': 'rooms/suite1_600_001.jpg'},
                {'name': 'Luxury Suite 2', 'price': 160, 'capacity': 3, 'equipment': 'King Bed, Sofa, Desk, TV, Mini-fridge', 'image': 'rooms/suite2_600_002.jpg'},
                {'name': 'Luxury Suite 3', 'price': 170, 'capacity': 3, 'equipment': 'King Bed, Sofa, Desk, TV, Mini-fridge', 'image': 'rooms/suite3_600_003.jpg'},
                {'name': 'Luxury Suite 4', 'price': 180, 'capacity': 3, 'equipment': 'King Bed, Sofa, Desk, TV, Mini-fridge', 'image': 'rooms/suite4_600_004.webp'},
                {'name': 'Luxury Suite 5', 'price': 200, 'capacity': 3, 'equipment': 'King Bed, Sofa, Desk, TV, Mini-fridge', 'image': 'rooms/suite5_600_005.jpg'},
            ],
        }

        for category, room_list in categories.items():
            for room_data in room_list:
                Room.objects.create(
                    name=room_data['name'],
                    price=room_data['price'],
                    capacity=room_data['capacity'],
                    equipment=room_data['equipment'],
                    image=room_data['image'],
                )
                self.stdout.write(self.style.SUCCESS(f"Room '{room_data['name']}' created."))
