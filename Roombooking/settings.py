import os
from pathlib import Path
import dj_database_url

# Project base directory
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Secret key (use environment variable for production!)
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'up(iut2n@m9!tr1*xbzrs*m+zsiuv6)^od9rjgo$bz(h4zi2_9'
)

# Debug mode — for production, set to False!
DEBUG = True

# Allowed hosts for local dev
ALLOWED_HOSTS = ['*']

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your application
    'booking',

    # For crispy-forms
    'crispy_forms',
    'crispy_bootstrap5',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Main URL config
ROOT_URLCONF = 'Roombooking.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # your template folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # needed for auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'Roombooking.wsgi.application'

# Database: use dj_database_url to parse DATABASE_URL or fallback to default
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:Postgres123!@db:5432/roombooking_db'
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False        # We'll define custom date format
USE_TZ = True

# Custom date input/output formats (English style)
DATE_FORMAT = "m/d/Y"                 # For display
DATETIME_FORMAT = "m/d/Y H:i"         # For display with time
DATE_INPUT_FORMATS = ['%m/%d/%Y']     # For forms input
DATETIME_INPUT_FORMATS = ['%m/%d/%Y %H:%M']

# Static files (CSS, JS, images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'booking' / 'static',
]

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Crispy forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Redirects after login/logout
LOGIN_REDIRECT_URL = '/my-bookings/'
LOGOUT_REDIRECT_URL = '/'
