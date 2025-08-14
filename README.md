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

## 🚀 Updates — Stage 4: Booking Validations & UI Improvements (August 13, 2025)

- ✅ Implemented unique booking validation for users to prevent overlapping bookings of the same room within conflicting dates  
- ✅ Added `created_at` field to the `Booking` model to store booking creation timestamp  
- ✅ Enhanced booking form with custom validation ensuring `check_in` date is before `check_out` date  
- ✅ Display success and error messages to users during booking via flash messages  
- ✅ Updated templates to properly show messages, improved styling and navigation flow  
- ✅ Refined views to handle booking logic securely and correctly  
- ✅ Tested the project thoroughly in Docker environment, updated README with clear local development instructions  

🔗 **Pull Request:**  
[Stage 4: Booking Validations & UI Improvements](https://github.com/OleksandrLapshin564/Roombooking/pull/2)

---

## 🚀 Updates — Stage 5: Final Post-Test & Stability (August 14, 2025)

- ✅ Completed final post-test checklist verifying full stability of the project  
- ✅ Checked Docker containers, navigation, authentication, and booking functionality  
- ✅ Ensured `Booking` model and `BookingForm` correctly handle overlapping dates and prevent `None` values in queries  
- ✅ Confirmed all pages load without errors and flash messages display correctly  
- ✅ Updated README.md and PROJECT_HISTORY.md to document the final stable version

🔗 **GitHub Branch:**  
[Final Stable Version - bootstrap-enhancement](https://github.com/OleksandrLapshin564/Roombooking/tree/bootstrap-enhancement)

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
docker-compose exec web python manage.py migrate

Create a superuser for admin access:
docker-compose exec web python manage.py createsuperuser

Open in your browser:

Homepage: http://localhost:8000/

Admin panel: http://localhost:8000/admin/

To stop containers:
docker-compose down

How to Check Media (Room Photos) Display

To ensure that uploaded room images are displayed correctly:

Verify images are present in the media/room_photos/ directory inside your project.

Check Django settings for media:
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

Confirm media URLs are served during development in urls.py:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your url patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Upload images via Django admin panel (/admin).

Visit room detail pages to see images.

Troubleshoot 404 errors or missing images by checking Docker volume mounts and media paths.

📁 Project Structure
booking/                  ← Main Django app
├── migrations/           ← Database migrations
├── models.py             ← Models: Category, Equipment, Room, Booking, Rating
├── templates/booking/    ← HTML templates
├── static/booking/       ← Static files (CSS, favicon, images)
├── views.py              ← View logic
├── admin.py              ← Admin configurations
├── forms.py              ← Forms definitions
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

📅 Last Updated: August 14, 2025