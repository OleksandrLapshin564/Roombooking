RoomBooking Project

RoomBooking is a simple training project built using Django, Docker, and PostgreSQL. It allows users to view a list of rooms, see details about each room, and access an "About Us" page. This project is developed as part of a learning process and will be gradually extended with more functionality.

🚀 Features Implemented

Responsive room listing page (/)

Room detail pages (/rooms/<id>/)

About Us page (/about/)

Base template using Bootstrap 5

Custom CSS styling (styles.css)

Favicon support

Clean and modular structure using Django app booking

⚙️ Technologies Used

Python 3.9.6

Django 4.2.x

PostgreSQL (via Docker)

Docker + Docker Compose

Bootstrap 5 (via CDN)

Static files (CSS + favicon)
📁 Project Structure
Roombooking/
├── booking/                    # Main Django app
│   ├── templates/booking/     # HTML templates
│   │   ├── base.html
│   │   ├── room_list.html
│   │   ├── room_detail.html
│   │   └── about.html
│   ├── static/booking/        # Static assets
│   │   ├── styles.css
│   │   └── images/favicon.ico
│   ├── views.py               # Django views
│   ├── urls.py                # App routes
│   └── ...
├── Roombooking/               # Django project config
│   ├── settings.py
│   ├── urls.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── manage.py

🐳 Docker Instructions

Build and Run the Containers
docker-compose up --build
Stop Containers
docker-compose down
Run Django Commands in Web Container
docker-compose run web python manage.py <command>
Example:
docker-compose run web python manage.py migrate
Create Superuser
docker-compose run web python manage.py createsuperuser
🔎 Testing

All views are accessible via browser:

http://localhost:8000/ → Room list

http://localhost:8000/rooms/1/ → Room detail

http://localhost:8000/about/ → About page

Templates are rendered correctly.

Bootstrap and custom styles load properly.

Favicon is displayed.

Layout adapts responsively to different screen sizes.
📦 Archiving Notes

Before submitting:

All __pycache__ folders were deleted

.venv/ and .idea/ were excluded

Archive is named: roombooking_project_Oleksa.rar

Total archive size is under 25MB
🧭 Future Enhancements

Add room images

Use dynamic database-driven room data

Implement booking forms

Extend admin functionality

Add 404 and error handling pages

📝 Author

Oleksa (Student)

📅 Last Updated

08 July 2025

