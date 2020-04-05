from .base import *

import json

from django.core.exceptions import ImproperlyConfigured

# Secure Secret Key Logic

# JSON-based secrets module
with open(os.path.join(BASE_DIR, 'secrets.json')) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {0} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)


# Basic Settings

SECRET_KEY = get_secret('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']

# Installed Apps

INSTALLED_APPS += [
    'core',
    'website',
]

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_project_db',
        'USER': get_secret('POSTGRES_USER'),
        'PASSWORD': get_secret('POSTGRES_PASSWORD'),
        'HOST': 'postgres.example.com',
        'PORT': '5432',
    }
}

# Static Files

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media Uploads

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email Backend

EMAIL_HOST = "mail.example.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Login Settings

LOGIN_URL = 'core:login'
LOGOUT_REDIRECT_URL = 'website:home_page'

# Google ReCaptcha

RECAPTCHA_SECRET_KEY = get_secret('RECAPTCHA_SECRET_KEY')
RECAPTCHA_SITE_KEY = get_secret('RECAPTCHA_SITE_KEY')

# 2020.04.01-DEA
