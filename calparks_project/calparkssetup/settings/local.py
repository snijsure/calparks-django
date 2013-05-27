
from .base import *

DEBUG = True
COMPRESS_ENABLED = True
TEMPLATE_DEBUG = DEBUG

#DEBUG_APPS += [
#    'debug_toolbar',
#]

#MIDDLEWARE_CLASSES += (
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
#)

#DEBUG_TOOLBAR_PANELS = (
#    'debug_toolbar.panels.version.VersionDebugPanel',
#    'debug_toolbar.panels.timer.TimerDebugPanel',
#    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#    'debug_toolbar.panels.headers.HeaderDebugPanel',
#    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#    'debug_toolbar.panels.template.TemplateDebugPanel',
#    'debug_toolbar.panels.sql.SQLDebugPanel',
#    'debug_toolbar.panels.signals.SignalDebugPanel',
#    'debug_toolbar.panels.logger.LoggingPanel',
#)

INSTALLED_APPS += (
     'rest_framework',
#     'compressor',
)

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


# Emails
# =======
EMAIL_SUBJECT_PREFIX = '[LOCAL ]'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
