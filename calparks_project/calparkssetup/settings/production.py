from .base import *

DEBUG = True
COMPRESS_ENABLED = True
TEMPLATE_DEBUG = DEBUG

# Databases
# ==========

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'calparks',                      # Or path to database file if using sqlite3.
        'USER': 'calparks',                      # Not used with sqlite3.
        'PASSWORD': 'calparks25',                  # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += (
     'rest_framework',
#     'compressor',
)
STATIC_ROOT = "/var/www/static_dev"
