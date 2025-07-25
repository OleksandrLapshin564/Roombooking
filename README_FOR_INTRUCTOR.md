# 📬 Submission Note – RoomBooking Project (Stage 2)

Dear Instructor,

This is my completed submission for **RoomBooking – Stage 2** of the Django course.

## 📌 Contents of the Archive

- Full Django project with:
  - `booking` app (includes templates, static files, routes)
  - Custom templates: `base.html`, `room_list.html`, `room_detail.html`, `about.html`
  - Bootstrap and custom CSS integration
  - Static favicon and CSS handled via Django `static` directory
- Working Docker configuration (`Dockerfile` + `docker-compose.yml`)
- `README.md` with setup instructions
- `PROJECT_HISTORY.md` showing progress and completed tasks
- `__pycache__`, `.idea/`, and `.venv/` excluded to keep size <25MB

## ✅ Tested Features

- Room list and detail pages display correctly
- Fully responsive layout with Bootstrap
- About page styled with custom CSS
- All routes tested:
  - `/`
  - `/rooms/<id>/`
  - `/about/`

## 🛠️ Run Instructions

To build and run:

```bash
docker-compose up --build

Then open in browser:
http://localhost:8000/

Thank you for your time and feedback!

Sincerely,
Oleksa Lapshyn