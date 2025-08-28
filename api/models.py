from django.core.management.base import BaseCommand
from booking.models import Room

class Command(BaseCommand):
    help = 'Populate the database with 15 sample rooms (5 per category)'

    def handle(self, *args, **kwargs):
        # Room categories
        categories = {
            'Single': [
                {'name': 'Single Cozy', 'price': 50, 'description': 'Comfortable single room.', 'equipment': 'Bed, Desk, Chair', 'image': 'rooms/single1.jpg'},
                {'name': 'Single Modern', 'price': 55, 'description': 'Modern single room with all amenities.', 'equipment': 'Bed, Desk, TV', 'image': 'rooms/single2.jpg'},
                {'name': 'Single Standard', 'price': 45, 'description': 'Standard single room.', 'equipment': 'Bed, Wardrobe', 'image': 'rooms/single3.jpg'},
                {'name': 'Single Compact', 'price': 40, 'description': 'Compact room for one.', 'equipment': 'Bed, Desk', 'image': 'rooms/single4.jpg'},
                {'name': 'Single Deluxe', 'price': 60, 'description': 'Deluxe single room with extras.', 'equipment': 'Bed, Desk, TV, Mini-fridge', 'image': 'rooms/single5.jpg'},
            ],
            'Double': [
                {'name': 'Double Cozy', 'price': 80, 'description': 'Comfortable double room.', 'equipment': '2 Beds, Desk, Chair', 'image': 'rooms/double1.jpg'},
                {'name': 'Double Modern', 'price': 90, 'description': 'Modern double room with amenities.', 'equipment': '2 Beds, Desk, TV', 'image': 'rooms/double2.jpg'},
                {'name': 'Double Standard', 'price': 75, 'description': 'Standard double room.', 'equipment': '2 Beds, Wardrobe', 'image': 'rooms/double3.jpg'},
                {'name': 'Double Compact', 'price': 70, 'description': 'Compact double room.', 'equipment': '2 Beds, Desk', 'image': 'rooms/double4.jpg'},
                {'name': 'Double Deluxe', 'price': 100, 'description': 'Deluxe double room with extras.', 'equipment': '2 Beds, Desk, TV, Mini-fridge', 'image': 'rooms/double5.jpg'},
            ],
            'Luxury': [
                {'name': 'Luxury Suite 1', 'price': 200, 'description': 'Luxury suite with king-size bed.', 'equipment': 'King Bed, Sofa, TV, Mini-bar', 'image': 'rooms/luxury1.jpg'},
                {'name': 'Luxury Suite 2', 'price': 220, 'description': 'Spacious luxury suite.', 'equipment': 'King Bed, Desk, TV, Mini-bar', 'image': 'rooms/luxury2.jpg'},
                {'name': 'Luxury Suite 3', 'price': 210, 'description': 'Elegant luxury suite.', 'equipment': 'King Bed, Sofa, Desk, TV', 'image': 'rooms/luxury3.jpg'},
                {'name': 'Luxury Suite 4', 'price': 230, 'description': 'Premium luxury suite.', 'equipment': 'King Bed, Sofa, TV, Mini-bar, Desk', 'image': 'rooms/luxury4.jpg'},
                {'name': 'Luxury Suite 5', 'price': 250, 'description': 'Top-class luxury suite.', 'equipment': 'King Bed, Sofa, TV, Mini-bar, Jacuzzi', 'image': 'rooms/luxury5.jpg'},
            ],
        }

        # Create rooms in the database
        for category, rooms in categories.items():
            for room_data in rooms:
                room, created = Room.objects.get_or_create(
                    name=room_data['name'],
                    defaults={
                        'description': room_data['description'],
                        'price': room_data['price'],
                        'capacity': 1 if category == 'Single' else 2 if category == 'Double' else 4,
                        'equipment': room_data['equipment'],
                        'image': room_data['image'],  # Make sure MEDIA_ROOT/rooms/... exists
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Room '{room.name}' created."))
                else:
                    self.stdout.write(self.style.WARNING(f"Room '{room.name}' already exists."))
