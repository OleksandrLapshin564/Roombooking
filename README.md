# RoomBooking Project

**Project Overview:**  
RoomBooking is a Django-based web application for booking hotel rooms. It supports guest access, registered users, and admin management, with integrated REST API and Swagger documentation.

**Project Repository:** [https://github.com/OleksandrLapshin564/Roombooking](https://github.com/OleksandrLapshin564/Roombooking)

---

## Project Timeline

- **Stage 1: Project Setup (2025-07-05 — 2025-07-07)**
  - Created Django project `Roombooking`.
  - Configured Docker and PostgreSQL.

- **Stage 2: Templates & Static Files (2025-07-07 — 2025-07-10)**
  - Developed `base.html`, `room_list.html`, `room_detail.html`.
  - Integrated Bootstrap and custom CSS.

- **Stage 3: Models & Admin (2025-08-03 — 2025-08-05)**
  - Created `Room` and `Booking` models.
  - Configured admin panel for rooms and bookings.
  - Uploaded 15 initial rooms (single, double, suite).

- **Stage 4: Categories & Filtering (2025-08-05 — 2025-08-06)**
  - Implemented room categories.
  - Added views and templates for filtering by type.

- **Stage 5: REST API (2025-08-20 — 2025-08-22)**
  - Added DRF endpoints (`/api/rooms/`).
  - Integrated Swagger UI (`/swagger/`).

- **Stage 6: Media & Images (2025-08-23 — 2025-08-29)**
  - Configured media file handling in Docker.
  - Added default image fallback.

- **Stage 7: Testing & Debugging (2025-08-29 — 2025-09-05)**
  - Verified web pages and REST API responses.
  - Ensured Docker containers run correctly.

- **Stage 8: Finalization (2025-09-05)**
  - All rooms display correctly.
  - API and Swagger documentation verified.
  - Prepared README.md and PROJECT_HISTORY.md.
  - Committed all changes to GitHub.

---

## Features

- View all available rooms and room details.
- Filter rooms by category (single, double, suite).
- Book rooms (admin and user management).
- REST API for room data.
- Swagger documentation for API testing.
- Dockerized development environment.

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/OleksandrLapshin564/Roombooking.git
cd Roombooking
2. Build and run Docker containers:
docker-compose build
docker-compose up -d
3. Access the site: 
Frontend: http://localhost:8001/
Admin panel: http://localhost:8001/admin/
API: http://localhost:8001/api/rooms/
Swagger: http://localhost:8001/swagger/