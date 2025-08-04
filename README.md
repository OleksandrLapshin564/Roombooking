# 🏨 RoomBooking

RoomBooking is a Django-based web application that allows users to view and book available rooms.

## 🛠 Features

- Responsive room list and detail pages
- Django templating with **Bootstrap 5**
- Static and uploaded images for room previews
- **Database models** for Room and Booking
- **Admin interface** for managing rooms and bookings
- **Media handling** with Pillow (room photos)
- Dockerized environment for easy local development

---

## 🚀 What's New — Stage 2: UI & Models Enhancement (July 2025)

- ✅ Modernized layout with **Bootstrap 5** (grid, cards, containers)
- ✅ Redesigned `room_list.html` with responsive styling
- ✅ Replaced placeholder images with real room photos
- ✅ Added models `Room` and `Booking`
- ✅ Populated database with 15 rooms (5 single, 5 double, 5 luxury) via admin
- ✅ Connected media handling with `MEDIA_URL` and `MEDIA_ROOT`
- ✅ Enabled image upload support in Docker + Pillow installed
- ✅ Updated templates: `base.html`, `room_list.html`, `room_detail.html`
- ✅ Cleaned up and structured static and media files

🔗 **Pull Request:**  
[UI & Models Update on GitHub](https://github.com/OleksandrLapshin564/Roombooking/pull/1)

---

## 🐳 Local Development with Docker

### ▶️ Start Project

```bash
docker-compose up --build
Visit the app at:
📍 http://localhost:8000

🛑 Stop Containers
bash
Копировать
Редактировать
docker-compose down
📁 Project Structure
swift
Копировать
Редактировать
booking/                ← Main Django app
├── models.py           ← Room & Booking models
├── templates/booking/  ← HTML templates
├── static/booking/     ← CSS, favicon, images
├── views.py            ← Room list & detail views

media/                  ← Uploaded room images
Dockerfile              ← Django + Pillow
docker-compose.yml      ← Dev setup (includes PostgreSQL)
🔒 Admin Panel (Local Testing)
Access: http://localhost:8000/admin/

Superuser: created during setup (Oleksa)

📦 Requirements
See requirements.txt for full package list:

Django>=4.2,<5.0

Pillow>=9.0.0

psycopg2-binary

others...

🧪 Testing Checklist (Stage 2 Complete)
✅ Django templates structured and extended properly

✅ Bootstrap 5 loaded via CDN

✅ Static room images show correctly

✅ Media upload via admin works (tested in Docker)

✅ Database models created and migrated

✅ Admin panel works for Room & Booking

📤 Submitted For Instructor Review
✅ GitHub Repository

✅ Pull Request with Changes

📅 Last Updated: 04 August 2025
yaml

