from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from booking import api_views

# --- DRF router ---
router = routers.DefaultRouter()
router.register(r'rooms', api_views.RoomViewSet, basename='room')
router.register(r'bookings', api_views.BookingViewSet, basename='booking')
router.register(r'categories', api_views.CategoryViewSet, basename='category')
router.register(r'equipments', api_views.EquipmentViewSet, basename='equipment')

# --- URL patterns ---
urlpatterns = [
    path('admin/', admin.site.urls),

    # HTML-based app routes
    path('', include('booking.urls')),

    # API routes
    path('api/', include(router.urls)),

    # DRF auth routes (optional, for browsable API login/logout)
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    # Serve uploaded media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
