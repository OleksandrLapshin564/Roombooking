# Roombooking Project

## Overview
Roombooking is a Django-based web application for managing hotel room reservations. It includes user registration, booking forms, rating system, and category views.

## Stage 3: OpenAI Integration
- Added an "OpenAI API Test" page.
- Integrated mock responses from OpenAI for safe testing.
- Users can submit prompts and see AI-generated responses.
- Mock responses are used instead of real API calls to avoid costs.

## Features
- Room listing and detail pages.
- Booking and rating forms.
- Categories and filtering by room type.
- User registration and login.
- OpenAI API test with mock responses.

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/OleksandrLapshin564/Roombooking.git
2. Set up .env with your environment variables (including OPENAI_API_KEY).
3. Run using Docker: 
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
4. Access the site at http://127.0.0.1:8001/.
License

This project is for educational purposes.