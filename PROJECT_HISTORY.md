# Project History — RoomBooking

---

### ✅ Stage 4 Enhancement — Ratings, Availability & Equipment (09.08.2025)

- Added `Rating` model linked to rooms and users to enable user feedback.
- Added `is_available` boolean field to Room model to indicate booking availability.
- Introduced `Equipment` model with many-to-many relation to Room for listing available equipment.
- Updated admin panel to manage ratings, equipment, and room availability.
- Modified templates to display equipment lists, availability status, and ratings on room detail pages.
- Updated Docker setup and `docker-compose.yml` to improve container orchestration.
- Created and applied migrations for new models and fields.
- Committed all changes under branch `bootstrap-enhancement` and pushed to GitHub.

---

### ✅ Stage 3 Enhancement — Category Integration (07.08.2025)

- Added `Category` model to classify rooms into Single, Double, and Luxury.
- Updated models, views, and templates to support category filtering and display.
- Designed `category_list.html` and `rooms_by_category.html` templates.
- Ensured navigation flow from main page categories to filtered room lists.
- Configured media files handling (`MEDIA_ROOT`, `MEDIA_URL`) for room images.
- Fully dockerized setup with Pillow image library installed.

🔗 Pull Request: https://github.com/OleksandrLapshin564/Roombooking/pull/1

---

### ✅ Stage 2 Complete — Bootstrap UI (29.07.2025)

- Improved visual layout using Bootstrap 5.
- Redesigned `room_list.html` to use card-based responsive grid layout.
- Added static images and sample room previews.
- Connected Bootstrap via CDN in `base.html`.
- Updated Docker setup and static file paths.
- Added backup version of `room_list.html` for comparison.
- README.md updated with PR info.
- Pull Request: https://github.com/OleksandrLapshin564/Roombooking/pull/1

---

### ✅ Stage 1 Complete — Basic Django Setup (до 07.07.2025)

- Created Django app `booking`.
- Set up project structure with static and template folders.
- Created views and templates: `base.html`, `room_list.html`, `room_detail.html`.
- Dockerized Django environment.
- Connected routing and created initial static room data.

---

📘 Project History and Progress Log

This file helps to track completed tasks and future plans.

📁 Project Name: **RoomBooking**

---

✅ Completed Tasks

- Initialized Django project Roombooking.
- Created Docker configuration (`Dockerfile`, `docker-compose.yml`).
- Configured PostgreSQL database in Docker.
- Applied initial Django migrations.
- Created superuser (`Oleksa`) and accessed Django admin panel.
- Created the `/about/` route with a simple HTML response.
- Verified all routes (`/`, `/admin/`, `/about/`).
- Prepared and submitted archive `roombooking_project_Oleksa.rar`.
- Integrated Bootstrap 5 and custom `styles.css`.
- Finalized templates: `base.html`, `room_list.html`, `room_detail.html`, `about.html`.
- Refactored frontend with Bootstrap cards and grid system.
- Created and registered Django models.
- Populated room data with images using admin interface.
- Served uploaded media in Docker using volume and configuration.
- Updated templates to use dynamic data from models.
- Added category grouping and filtering functionality.
- Added rating system, equipment model, and room availability status.
- Improved Docker container orchestration and migrations.

---

📌 Next Steps (Future)

- Implement room booking form and save to `Booking` model.
- Add date availability and filtering by room type.
- Create user registration and authentication.
- Add booking confirmation view and email notification.
- Add custom admin model display (list display, filters).
- Improve UX (loading indicators, empty states, tooltips).
- Implement pagination and search in room list.
- Add unit tests and basic automated test coverage.

---

🗓 Last Updated: **09 August 2025**
