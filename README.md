# 🏨 RoomBooking

RoomBooking is a Django-based web application that allows users to browse and book rooms categorized into Single, Double, and Luxury types.

---

## 🛠 Key Features

- Homepage displaying room categories instead of all rooms at once
- Viewing rooms filtered by category
- Detailed room page with description, price, capacity, and image
- Admin panel to manage categories, rooms, and bookings
- Image upload support for rooms via admin interface
- Stable operation via Docker with PostgreSQL
- Basic styling using Bootstrap 5

---

## 🚀 Updates — Stage 2: Categories & UI (August 2025)

- ✅ Added `Category` model for grouping rooms
- ✅ Homepage shows categories instead of full room list
- ✅ Rooms filtered by selected category
- ✅ Updated templates: `category_list.html`, `rooms_by_category.html`, `room_detail.html`
- ✅ Enhanced admin panel with category management
- ✅ Configured media files for room images (`MEDIA_ROOT` and `MEDIA_URL`)
- ✅ Fully dockerized setup with image upload and Pillow installed

🔗 **Pull Request:**  
[Stage 2: Categories & UI Enhancement](https://github.com/OleksandrLapshin564/Roombooking/pull/1)

---

## 🐳 Local Development with Docker

### Startup steps:

1. Clone the repository and enter the project folder:
```bash
git clone https://github.com/OleksandrLapshin564/Roombooking.git
cd Roombooking
Build and start containers:


docker-compose up -d --build
Run migrations:


docker exec -it roombooking-web-1 python manage.py migrate
Create a superuser for admin access:


docker exec -it roombooking-web-1 python manage.py createsuperuser
Open in your browser:
Homepage: http://localhost:8000/
Admin panel: http://localhost:8000/admin/

To stop containers:
docker-compose down
📁 Project Structure
pgsql
Copy
Edit
booking/                ← Main Django app
├── migrations/         ← Database migrations
├── models.py           ← Models: Category, Room, Booking
├── templates/booking/  ← HTML templates (category_list, rooms_by_category, room_detail, etc.)
├── static/booking/     ← Static files (CSS, favicon, images)
├── views.py            ← View logic
├── admin.py            ← Admin configurations
media/                  ← Uploaded room images (mounted in Docker)
Dockerfile              ← Django + Pillow image setup
docker-compose.yml      ← Docker configuration for web server and PostgreSQL
manage.py               ← Django management script
🛠 Technologies Used
Python 3.x, Django 4.x

PostgreSQL (via Docker)

Docker & Docker Compose

Bootstrap 5

Pillow for image handling

⚙️ Future Plans & Recommendations
Improve styling and UX (separate style-enhancement branch)

Add filters and search for rooms

Optimize image upload and display

Implement booking confirmation system

Document project history and changes (PROJECT_HISTORY.md)

📬 Contact
Author: Oleksandr Lapshin
Email: lapshin.oleksa@gmail.com

📅 Last Updated: August 7, 2025
