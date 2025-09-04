# booking/management/commands/populate_rooms.py

from django.core.management.base import BaseCommand
from booking.models import Room
from django.core.files import File
from pathlib import Path

class Command(BaseCommand):
    help = "Populate the database with 15 rooms with correct images"

    def handle(self, *args, **kwargs):
        media_path = Path("media/rooms")

        rooms_data = [
            # --- Single Rooms ---
            {"name": "Single Cozy", "room_type": "single", "description": "Cozy single room", "equipment": "Bed, Desk, Chair", "price": 50, "image": "sng_600_001_Pq8ckdh.jpg"},
            {"name": "Single Modern", "room_type": "single", "description": "Modern single room", "equipment": "Bed, Desk, Chair, TV", "price": 55, "image": "sng_600_002_K7mYbyq.jpg"},
            {"name": "Single Classic", "room_type": "single", "description": "Classic single room", "equipment": "Bed, Wardrobe, Desk", "price": 60, "image": "sng_600_003_LIxFK05.jpg"},
            {"name": "Single Compact", "room_type": "single", "description": "Compact single room", "equipment": "Bed, Chair", "price": 48, "image": "sng_600_004_Q1dR9i2.jpg"},
            {"name": "Single Deluxe", "room_type": "single", "description": "Deluxe single room", "equipment": "Bed, Desk, Chair, TV, Mini-fridge", "price": 70, "image": "sng_600_005_8GujQxM.jpg"},

            # --- Double Rooms ---
            {"name": "Double Cozy", "room_type": "double", "description": "Cozy double room", "equipment": "2 Beds, Desk, Chair", "price": 80, "image": "db1_600_001_uUb1gfj.webp"},
            {"name": "Double Modern", "room_type": "double", "description": "Modern double room", "equipment": "2 Beds, Desk, Chair, TV", "price": 85, "image": "db2_600_002_GJ7wE7r.jpg"},
            {"name": "Double Classic", "room_type": "double", "description": "Classic double room", "equipment": "2 Beds, Wardrobe, Desk", "price": 90, "image": "db3_600_003_MDTxq00.jpg"},
            {"name": "Double Compact", "room_type": "double", "description": "Compact double room", "equipment": "2 Beds, Chair", "price": 78, "image": "db4_600_004_HY1eBiE.webp"},
            {"name": "Double Deluxe", "room_type": "double", "description": "Deluxe double room", "equipment": "2 Beds, Desk, Chair, TV, Mini-fridge", "price": 100, "image": "db5_600_005_BeaIdW2.webp"},

            # --- Luxury Suites ---
            {"name": "Luxury Suite 1", "room_type": "suite", "description": "Luxury Suite 1", "equipment": "King Bed, Sofa, Desk, TV, Mini-fridge", "price": 150, "image": "suite1_600_001_lAnmggH.jpg"},
            {"name": "Luxury Suite 2", "room_type": "suite", "description": "Luxury Suite 2", "equipment": "King Bed, Sofa, Desk, TV, Mini-fridge", "price": 160, "image": "suite2_600_002_E875Hrb.jpg"},
            {"name": "Luxury Suite 3", "room_type": "suite", "description": "Luxury Suite 3", "equipment": "King Bed, Sofa, Desk, TV, Mini-fridge", "price": 170, "image": "suite3_600_003_6eqApDt.jpg"},
            {"name": "Luxury Suite 4", "room_type": "suite", "description": "Luxury Suite 4", "equipment": "King Bed, Sofa, Desk, TV, Mini-fridge", "price": 180, "image": "suite4_600_004_l2JenHT.webp"},
            {"name": "Luxury Suite 5", "room_type": "suite", "description": "Luxury Suite 5", "equipment": "King Bed, Sofa, Desk, TV, Mini-fridge", "price": 200, "image": "suite5_600_005_sKsNHDx.jpg"},
        ]

        for room_data in rooms_data:
            room, created = Room.objects.get_or_create(
                name=room_data["name"],
                defaults={
                    "room_type": room_data["room_type"],
                    "description": room_data["description"],
                    "equipment": room_data["equipment"],
                    "price": room_data["price"],
                },
            )

            # Attach image
            image_path = media_path / room_data["image"]
            if image_path.exists():
                with open(image_path, "rb") as f:
                    room.image.save(room_data["image"], File(f), save=True)

            if created:
                self.stdout.write(self.style.SUCCESS(f"Room '{room.name}' created."))
            else:
                self.stdout.write(self.style.WARNING(f"Room '{room.name}' already exists."))
