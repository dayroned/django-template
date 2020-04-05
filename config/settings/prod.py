from .base import *

"""
Django Prod Settings

"""

DEBUG = False

ALLOWED_HOSTS = ["*.localhost", "localhost"]

# Media Uploads

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Email Backend

EMAIL_HOST = "localhost"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Security

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
