from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "booking"  # namespace to avoid conflicts

urlpatterns = [
    # ---------------------------
    # Main pages
    # ---------------------------
    path("", views.room_list, name="room_list"),
    path("rooms/<int:room_id>/", views.room_detail, name="room_detail"),
    path("about/", views.about, name="about"),

    # ---------------------------
    # Categories
    # ---------------------------
    path("categories/", views.category_list, name="category_list"),
    path("categories/<str:room_type>/", views.rooms_by_category, name="rooms_by_category"),

    # ---------------------------
    # Authentication
    # ---------------------------
    path("login/", auth_views.LoginView.as_view(template_name="booking/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", views.register, name="register"),

    # ---------------------------
    # Password reset
    # ---------------------------
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(template_name="booking/password_reset.html"),
        name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="booking/password_reset_done.html"),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="booking/password_reset_confirm.html"),
        name="password_reset_confirm"
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(template_name="booking/password_reset_complete.html"),
        name="password_reset_complete"
    ),
]
