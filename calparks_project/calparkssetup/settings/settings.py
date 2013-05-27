# Django settings for calparks project.
from unipath import FSPath as Path

PROJECT_DIR = Path(__file__).absolute().ancestor(1)

SITE_ID = 1
DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

# ----------------
# Paths/Dirs/urls
# ----------------
MEDIA_ROOT = PROJECT_DIR.child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '/static/'  # If this changes, then modify hardcoded url in geo.js
STATIC_DEV = PROJECT_DIR.child('static_dev')
STATICFILES_DIRS = (STATIC_DEV,)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ROOT_URLCONF = 'calparkssetup.urls'

# ---------------
# Authentication
# ---------------
ACCOUNT_ACTIVATION_DAYS = 7

AUTH_PROFILE_MODULE = 'accounts.UserProfile'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

#------------------------------
# Templates
#------------------------------

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'calparkssetup.context_processors.globals',
)

# Applications
PREREQ_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'registration',
    'easy_thumbnails',
    'pagination',
    'storages',
    'boto',
    'gcm',
]

PROJECT_APPS = [
    'calparks',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

ADMINS = (
    ('snijsure', 'subodh.nijsure@gmail.com'),
)

MANAGERS = ADMINS

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', 
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 300,
        'BINARY': True,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'stsp32-g3+i!4ijz9+2eytbxn2ezm+tdg(xd_6_^(*51c54^&amp;3'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'calparkssetup.wsgi.application'

GCM_KEYS = "AIzaSyDsNCtjDp2Lcf4obeAaHdbR6lvHtsvBCw4"


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

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

try:
    from local_settings import *
except ImportError:
    pass
