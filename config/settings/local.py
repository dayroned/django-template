from .base import *

"""
Django Local Settings

"""

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Email Backend

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "mailhog"
EMAIL_PORT = 1025
