# Project History - RoomBooking

## Stage 1: Project Setup (2025-07-05 — 2025-07-07)
- Created Django project `Roombooking`.
- Added `booking` app.
- Configured Docker and Docker Compose.
- Set up PostgreSQL database in Docker.

## Stage 2: Templates & Static Files (2025-07-07 — 2025-07-10)
- Created `base.html` with Bootstrap integration.
- Developed `room_list.html` and `room_detail.html`.
- Added static CSS and default images.
- Implemented navigation and footer.

## Stage 3: Models & Admin (2025-08-03 — 2025-08-05)
- Created `Room` and `Booking` models.
- Added fields: name, type, description, price, image.
- Configured admin panel for managing rooms and bookings.
- Uploaded initial data for 15 rooms (single, double, suite).

## Stage 4: Categories & Filtering (2025-08-05 — 2025-08-06)
- Implemented room categories: single, double, suite.
- Created category views and templates.
- Added URL patterns for filtering by category.

## Stage 5: REST API (2025-08-20 — 2025-08-22)
- Added Django REST Framework.
- Created API endpoints for listing rooms (`/api/rooms/`).
- Implemented Swagger documentation (`/swagger/`).

## Stage 6: Media & Images (2025-08-23 — 2025-08-29)
- Configured MEDIA_URL and MEDIA_ROOT.
- Added default image fallback for missing room photos.
- Tested image serving in Docker environment.

## Stage 7: Testing & Debugging (2025-08-29 — 2025-09-05)
- Verified all pages render correctly in browser.
- Ensured REST API returns correct JSON data.
- Checked Docker setup: `web` and `db` containers running.
- Fixed `wait-for-it.sh` and system package issues.

## Stage 8: Finalization (2025-09-05)
- Verified all rooms display properly.
- Confirmed Swagger and API endpoints work.
- Prepared README.md and PROJECT_HISTORY.md.
- Committed all changes to GitHub repository.
