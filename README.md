# RoomBooking REST API

RoomBooking is a **Django-based REST API project** for managing room bookings.  
Originally started as a Django + Bootstrap web application, the project has been **fully migrated to a REST API backend** (as of 19.08.2025).  
This design enables integration with external frontend frameworks (React, Vue, Angular) or mobile clients.

---

## 🛠 Features

- 🔑 User authentication & authorization (Django REST Framework ready)
- 🏢 Room management (list rooms, view details, capacity, descriptions)
- 📅 Booking management (create, view, and manage reservations)
- 🌐 RESTful endpoints with JSON responses
- 🐳 Fully Dockerized for development and testing

---

## 📡 REST API Endpoints

Example endpoints (prefix: `/api/`):

- `GET /api/rooms/` → List all rooms  
- `GET /api/rooms/{id}/` → Get room details  
- `POST /api/bookings/` → Create a booking  
- `GET /api/bookings/` → List all bookings  

---

## 🐳 Local Development (via Docker)

```bash
# Build and start containers
docker compose up --build

# Stop containers
docker compose down

Web API will be available at: http://localhost:8001/api/

PostgreSQL DB exposed at: localhost:5432

📁 Project Structure

Roombooking/
├── booking/               # Core Django app
│   ├── api/               # REST API (serializers, views, urls)
│   ├── migrations/        # DB migrations
│   └── models.py          # Database models
├── Roombooking/           # Django project settings
├── Dockerfile             # API container definition
├── docker-compose.yml     # Services (web, db)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
📜 Project Evolution

Initial phase → Django + Bootstrap frontend with templates

Intermediate → UI enhancements (Bootstrap 5, responsive layout)

Final phase (19.08.2025) → Full migration to REST API backend

Templates removed from main workflow

API-first architecture introduced

Ready for frontend/mobile integration

🧑‍🏫 Assignment Info

✅ Task: Convert RoomBooking project into a full REST API

📅 Completed: 19.08.2025

🔗 GitHub Repository: RoomBooking on GitHub

👨‍🏫 For instructor review: Denis Hennadiyovych