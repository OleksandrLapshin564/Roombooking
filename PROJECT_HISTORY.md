# Project History — RoomBooking

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


📘 Project History and Progress Log

This file helps to track what has been done and what is planned.

📁 Project Name

RoomBooking

✅ Completed Tasks

✅ Initialized Django project Roombooking.

✅ Created Docker configuration:

Dockerfile

docker-compose.yml

✅ Configured PostgreSQL database in Docker.

✅ Applied initial Django migrations.

✅ Created superuser:

Username: Oleksa

✅ Tested the Django admin panel successfully.

✅ Created the /about/ route with a simple HTML response.

✅ Verified routes work correctly (/admin/, /, and /about/).

✅ Prepared detailed README.md explaining:

How to build and run the project.

How to create migrations and a superuser.

How to stop containers.

Example docker-compose.yml.

✅ Deleted __pycache__ directories before archiving.

✅ Excluded .venv and .idea folders from the archive to keep size <25MB.

✅ Created and submitted archive roombooking_project_Oleksa.rar for instructor review.

✅ Created Django app booking and added it to INSTALLED_APPS.

✅ Created templates: base.html, room_list.html, room_detail.html, and about.html.

✅ Added static directory and integrated favicon.ico and custom styles.css.

✅ Successfully styled pages using Bootstrap 5 and custom CSS.

✅ Fully implemented and tested routes:

Home (/): Room list

Room detail (/rooms/<id>/)

About (/about/)

✅ Performed final visual testing in various screen sizes.

✅ Final results reviewed and confirmed to meet all Stage 2 homework requirements.

📌 Next Steps (Future)

Add images to rooms (static or from database).

Replace static data with dynamic data from the database.

Add forms for booking functionality.

Enhance the admin panel with custom models.

Improve error handling and 404 pages.

🗕️ Last Updated

08 July 2025

