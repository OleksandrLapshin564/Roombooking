# 📘 Project History and Progress Log

This file helps to track what has been done and what is planned.

---

## 📁 Project Name
**RoomBooking**

---

## ✅ Completed Tasks

- ✅ Initialized Django project `Roombooking`.
- ✅ Created Docker configuration:
  - `Dockerfile`
  - `docker-compose.yml`
- ✅ Configured PostgreSQL database in Docker.
- ✅ Applied initial Django migrations.
- ✅ Created superuser:
  - **Username:** Oleksa
- ✅ Tested the Django admin panel successfully.
- ✅ Created the `/about/` route with a simple HTML response.
- ✅ Verified routes work correctly (`/admin/`, `/`, and `/about/`).
- ✅ Prepared detailed `README.md` explaining:
  - How to build and run the project.
  - How to create migrations and a superuser.
  - How to stop containers.
  - Example `docker-compose.yml`.
- ✅ Deleted `__pycache__` directories before archiving.
- ✅ Excluded `.venv` and `.idea` folders from the archive to keep size <25MB.
- ✅ Created and submitted archive `roombooking_project_Oleksa.rar` for instructor review.
- ✅ Created Django app `booking` and added it to `INSTALLED_APPS`.
- ✅ Created templates: `base.html`, `room_list.html`, `room_detail.html`, and `about.html`.
- ✅ Added static directory and integrated `favicon.ico` and custom `styles.css`.
- ✅ Successfully styled pages using Bootstrap 5 and custom CSS.
- ✅ Fully implemented and tested routes:
  - Home (`/`): Room list
  - Room detail (`/rooms/<id>/`)
  - About (`/about/`)
- ✅ Performed final visual testing in various screen sizes.
- ✅ Final results reviewed and confirmed to meet all Stage 2 homework requirements.

---

## 🔄 Major Update — REST API Conversion (19.08.2025)

- ✅ Project fully migrated to **pure REST API architecture**.
- ✅ All existing Django templates and frontend logic removed.
- ✅ Added:
  - `booking/api/serializers.py`
  - `booking/api/views.py`
  - `booking/api/urls.py`
- ✅ Implemented API endpoints for:
  - Rooms listing (`/api/rooms/`)
  - Room details (`/api/rooms/<id>/`)
  - Bookings (`/api/bookings/`)
- ✅ Updated `docker-compose.yml` with consistent port mapping.
- ✅ Added `.gitignore` to project root.
- ✅ Committed and pushed full project history to GitHub (`rest-api` branch).

---

## 🗂 Architecture Overview after REST API Migration

```mermaid
flowchart TD
    subgraph Client ["Client Side (Frontend)"]
        A[Browser / React / Postman] -->|HTTP Requests| B
    end

    subgraph Backend ["Django REST API Backend"]
        B[API Endpoints /api/...]
        C[Views & Serializers]
        D[(PostgreSQL Database)]
        B --> C --> D
    end

Key difference:
The earlier HTML-based frontend (templates/, Bootstrap, static pages) is now removed.
Only REST API endpoints remain, designed for external clients (e.g., React frontend, Postman testing, mobile apps).
Next Steps (Future Work)

🚀 Build a React frontend (or another JS framework) to consume the REST API.

🚀 Add authentication (JWT or DRF TokenAuth).

🚀 Implement booking management via API (create/update/delete bookings).

🚀 Deploy project to cloud hosting (Heroku / Render / Railway).

🚀 Add automated testing for API endpoints.

🗕️ Last Updated

19 August 2025