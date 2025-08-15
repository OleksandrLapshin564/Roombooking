# 📜 Project History — RoomBooking

This document outlines the complete development history of the RoomBooking project, detailing updates, features, and improvements over time.

---

## Stage 1 — Initial Setup & Basic Models (August 5, 2025)

- ✅ Created Django project and `booking` app  
- ✅ Defined basic models: `Room`, `Booking`, `User`  
- ✅ Configured PostgreSQL database via Docker  
- ✅ Set up Docker environment for web and database services  
- ✅ Added initial templates and static files  
- ✅ Verified basic CRUD functionality for rooms and bookings  

---

## Stage 2 — Categories & UI Enhancement (August 7, 2025)

- ✅ Added `Category` model for room grouping  
- ✅ Updated homepage to show categories instead of all rooms  
- ✅ Added templates: `category_list.html`, `rooms_by_category.html`, `room_detail.html`  
- ✅ Enhanced admin panel to manage categories  
- ✅ Configured media files (`MEDIA_ROOT` and `MEDIA_URL`)  
- ✅ Fully dockerized setup with image upload support  

---

## Stage 3 — Ratings, Availability & Docker Enhancements (August 9, 2025)

- ✅ Added `Rating` model linked to rooms and users  
- ✅ Added `is_available` field to Room model  
- ✅ Added `Equipment` model and linked it to rooms (many-to-many)  
- ✅ Updated admin panel to manage ratings, availability, and equipment  
- ✅ Updated templates for detailed room display  
- ✅ Improved Docker orchestration in `docker-compose.yml`  
- ✅ Added migration files for new models and fields  

---

## Stage 4 — Booking Validations & UI Improvements (August 13, 2025)

- ✅ Implemented unique booking validation to prevent overlapping bookings  
- ✅ Added `created_at` timestamp field to `Booking` model  
- ✅ Enhanced booking form validation (`check_in` < `check_out`)  
- ✅ Displayed success/error messages to users via flash messages  
- ✅ Updated templates with better styling and navigation flow  
- ✅ Refined views for secure booking logic  
- ✅ Tested thoroughly in Docker environment  

---

## Stage 5 — Final Post-Test & Stability (August 14, 2025)

- ✅ Completed final post-test checklist verifying full project stability  
- ✅ Checked Docker containers, navigation, authentication, and booking functionality  
- ✅ Ensured `Booking` model and `BookingForm` correctly handle overlapping dates and prevent `None` queries  
- ✅ Confirmed all pages load without errors and flash messages display correctly  
- ✅ Updated README.md and PROJECT_HISTORY.md for final stable version  

---

## Stage 6 — API Testing & Automation (August 15, 2025)

- ✅ Added REST API endpoints for bookings (`GET`, `POST`, `PUT`, `DELETE`)  
- ✅ Implemented token-based authentication for API access  
- ✅ Created `serializers.py` and `api_views.py` to handle API data  
- ✅ Added `test_api.ps1` PowerShell script for automated API testing  
- ✅ Verified all CRUD operations for bookings via API in Docker environment  
- ✅ Updated README and PROJECT_HISTORY.md with API testing documentation  

---

## Branching & GitHub

- **bootstrap-enhancement**: Final stable version with all enhancements and API support  
- Pull Requests for stages documented in README.md  
- All migrations, models, views, templates, and scripts included  

---

## 🗓 Summary of Key Dates

- 05.08.2025 — Initial project setup, basic models  
- 07.08.2025 — Stage 2: Categories & UI  
- 09.08.2025 — Stage 3: Ratings, Availability & Docker enhancements  
- 13.08.2025 — Stage 4: Booking validations & UI improvements  
- 14.08.2025 — Stage 5: Final post-test & stability  
- 15.08.2025 — Stage 6: API testing & automation, final updates  

---

## Notes

- Project fully dockerized with PostgreSQL  
- Media files handled correctly via `MEDIA_ROOT` and `MEDIA_URL`  
- API endpoints fully functional for CRUD operations  
- PowerShell script included for automated API testing  

📬 Author: Oleksandr Lapshin  
Email: lapshin.oleksa@gmail.com  
Last Updated: August 15, 2025
