from django.urls import path
from .views import about_view, room_detail, category_list, rooms_by_category

urlpatterns = [
    path('', category_list, name='category_list'),  # Main page — list of categories
    path('category/<int:category_id>/', rooms_by_category, name='rooms_by_category'),  # Rooms by category
    path('about/', about_view, name='about'),  # "About us" page
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),  # Room details
]
