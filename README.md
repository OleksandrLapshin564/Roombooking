# Roombooking

## Project Overview
Roombooking is a Django-based web application designed for room booking management. It allows users to view rooms by category, see detailed information about each room including equipment, book rooms, and leave ratings. Admin users can manage rooms, equipment, bookings, and ratings via the Django admin interface.

## Features
- Display all rooms and filter by categories: Single, Double, Suite.
- Room details page with images, description, equipment list, booking form, and ratings.
- User authentication: Register, Login, Logout.
- Booking management for authenticated users.
- Rating system for rooms.
- Admin interface for managing rooms, equipment, bookings, and ratings.

## Project Structure
ect Structure
Roombooking/
├─ booking/ # Django app
│ ├─ migrations/ # Migration files
│ ├─ templates/booking/ # HTML templates
│ │ ├─ base.html
│ │ ├─ room_list.html
│ │ ├─ room_detail.html
│ │ ├─ category_list.html
│ │ ├─ rooms_by_category.html
│ │ ├─ about.html
│ │ ├─ register.html
│ │ └─ login.html
│ ├─ static/booking/ # Static files (CSS, JS, images)
│ ├─ admin.py
│ ├─ apps.py
│ ├─ forms.py
│ ├─ models.py
│ ├─ urls.py
│ └─ views.py
├─ media/ # Uploaded room images
├─ Roombooking/ # Project settings
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
├─ Dockerfile
├─ docker-compose.yml
├─ requirements.txt
└─ manage.py

## Technologies
- Python 3.9
- Django 4.2
- PostgreSQL
- Docker & Docker Compose
- Bootstrap 5 for frontend styling
- Pillow for image handling

## Setup Instructions
1. **Clone the repository**
```bash
git clone https://github.com/OleksandrLapshin564/Roombooking.git
cd Roombooking
2. Build and start Docker containers
docker-compose up -d --build
3. Apply migrations
docker-compose exec web python manage.py migrate
4. Create superuser for admin panel
docker-compose exec web python manage.py createsuperuser
5. Access the aplication
Frontend: http://localhost:8001/
Admin panel: http://localhost:8001/admin/
6. Optional: Stop containers
docker-compose down
Notes
Room images are stored in media/rooms/.

Equipment and room associations are handled via a Many-to-Many relationship in the Django models.

Categories: Single, Double, Suite.

Ensure Docker Desktop is running before starting the containers.

Future Improvements
Implement full REST API for rooms, bookings, and ratings.

Add automated tests for models and views.

Enhance UI with additional Bootstrap components.