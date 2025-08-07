import os
from pathlib import Path
from urllib.parse import urlparse

# Project base directory (two subdirectories from this file)
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Secret key (from the environment or default for dev mode)
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'up(iut2n@m9!tr1*xbzrs*m+zsiuv6)^od9rjgo$bz(h4zi2_9'
)

# Debug mode (False in production)
DEBUG = True

# Allowed hosts (change in production to specific domains)
ALLOWED_HOSTS = ['*']

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booking',  # ваш додаток
]

# Middleware layer
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL config
ROOT_URLCONF = 'Roombooking.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # global templates folder
        'APP_DIRS': True,  # global templates folder
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # adds request to templates
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = 'Roombooking.wsgi.application'

# Parsing DATABASE_URL (change in .env or Docker)
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgres://postgres:Postgres123!@db:5432/roombooking_db'
)

url = urlparse(DATABASE_URL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': url.path[1:],  # remove the leading /
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Location and time
LANGUAGE_CODE = 'en-us'

# You can change to your time zone, for example:
# TIME_ZONE = 'Europe/Kiev'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# Statics
STATIC_URL = '/static/'  # correct with trailing slash
STATIC_ROOT = BASE_DIR / 'staticfiles'  # directory for collectstatic in production
STATICFILES_DIRS = [
    BASE_DIR / 'booking' / 'static',
]

# Media (user uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
