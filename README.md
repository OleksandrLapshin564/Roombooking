# 🏨 RoomBooking

RoomBooking is a Django-based web application that allows users to browse and book rooms categorized into Single, Double, and Luxury types.

---

## 🛠 Key Features

- Homepage displaying room categories instead of all rooms at once  
- Viewing rooms filtered by category  
- Detailed room page with description, price, capacity, image, availability status, **and list of available equipment**  
- Admin panel to manage categories, rooms, bookings, **equipment**, and ratings  
- Image upload support for rooms via admin interface  
- Stable operation via Docker with PostgreSQL  
- Basic styling using Bootstrap 5  

---

## 🚀 Updates — Stage 2: Categories & UI (August 7, 2025)

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

## 🚀 Updates — Stage 3: Ratings, Availability & Docker Enhancements (August 9, 2025)

- ✅ Added `Rating` model linked to rooms and users  
- ✅ Added `is_available` boolean field to Room model  
- ✅ Added `Equipment` model and linked it to rooms (many-to-many)  
- ✅ Updated admin panel to manage ratings, room availability, and equipment  
- ✅ Modified templates for improved room details display, including availability and equipment list  
- ✅ Updated `docker-compose.yml` for better container orchestration  
- ✅ Added migration files for new models and fields  

---

## 🐳 Local Development with Docker

### Startup steps:

1. Clone the repository and enter the project folder:

```bash
git clone https://github.com/OleksandrLapshin564/Roombooking.git
cd Roombooking
Build and start containers:

bash

docker-compose up -d --build
Run migrations:

bash

docker-compose exec web python manage.py migrate
Create a superuser for admin access:

bash

docker-compose exec web python manage.py createsuperuser
Open in your browser:
Homepage: http://localhost:8000/
Admin panel: http://localhost:8000/admin/

To stop containers:

bash

docker-compose down
📸 How to Check Media (Room Photos) Display
To ensure that uploaded room images are displayed correctly in the project, follow these steps:

Check media files exist in the project folder:
Verify the images are present in the media/room_photos/ directory inside your project. You can list files using:

bash

ls media/room_photos/
Verify Django settings for media:
Make sure MEDIA_ROOT and MEDIA_URL are properly set in your settings.py:

python

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
Ensure URLs serve media during development:
In urls.py, confirm media files are served by adding:

python

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your url patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
Upload images via Django admin:
Use the admin panel (/admin) to upload images for rooms. Each room's image should be visible in the admin and frontend.

View images in the browser:
Visit the room detail pages on the frontend. Images should appear if everything is configured correctly.

Troubleshooting:
If images don't show, check browser developer console for 404 errors on media URLs. Verify Docker volumes mount the media directory correctly. Confirm the image files are present in the Docker container if using Docker.

📁 Project Structure
pgsql
Copy
Edit
booking/                  ← Main Django app
├── migrations/           ← Database migrations
├── models.py             ← Models: Category, Equipment, Room, Booking, Rating
├── templates/booking/    ← HTML templates (category_list, rooms_by_category, room_detail, etc.)
├── static/booking/       ← Static files (CSS, favicon, images)
├── views.py              ← View logic
├── admin.py              ← Admin configurations
media/                    ← Uploaded room images (mounted in Docker)
Dockerfile                ← Django + Pillow image setup
docker-compose.yml        ← Docker configuration for web server and PostgreSQL
manage.py                 ← Django management script
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

📅 Last Updated: August 9, 2025