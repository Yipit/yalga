#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from os.path import dirname, abspath, join
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

LOCAL_FILE = lambda *path: join(abspath(dirname(__file__)), *path)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'lunchgameapp',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
import dj_database_url

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = LOCAL_FILE('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = LOCAL_FILE('assets')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    LOCAL_FILE('static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4^2e!=dv44d10=4evkx3p$t39%fc17h3njfk$*pre_2%+@6jc$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgirun.application'

TEMPLATE_DIRS = (
    LOCAL_FILE('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'lunch',
)

if os.getenv('PORT'):
    os.environ['DATABASE_URL'] = os.getenv('HEROKU_POSTGRESQL_AMBER_URL')
    DATABASES['default'] = dj_database_url.config()

else:
    INSTALLED_APPS += (
        'unclebob',
    )
    TEST_RUNNER = 'unclebob.runners.Nose'
    import unclebob
    unclebob.take_care_of_my_tests()

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

PEOPLE = [
    "Vin Vacanti",
    "Jim Moran",
    "Zach Smith",
    "Nitya Oberoi",
    "Steve Pulec",
    "Dave Tomback",
    "Henry Xie",
    "Kelly Byrne",
    "Unaiz Kabani",
    "Joe Johnson",
    "Mingwei Gu",
    "Gabriel Falcao",
    "Andrew Gross",
    "Suneel Chakravorty",
    "Alice Li",
    "Sean Spielberg",
    "Laura Groetzinger",
    "Lincoln de Sousa",
    "Emily Tiernan",
    "Allen Yang",
    "Rumela Das",
    "Jordan Milan",
    "Matt Raoul",
    "Michelle Scharfstein",
    "Hugo Tavares"
]

RESTAURANTS = [
    ("Laut", 50),
    ("Qi", 50),
    ("Meatball Shop", 50),
    ("Ootoya", 50),
    ("Westville", 50),
    ("BLT Burger", 50),
    ("Num Pang", 50),
    ("Shake Shack", 50),
    ("Rosa Mexicana", 50),
    ("Grimaldis", 50),
    ("Vapiano", 50),
    ("Lillie's", 50),
    ("Coffee Shop", 50),
    ("El Cocotero", 50),
    ("Bareburger", 50),

    # these are the fancy ones :)
    ("No. 7 Sub", 100),
    ("Stix", 100),
    ("ABC Cocina", 100),
    ("Ippudo", 100),
    ("Gramercy Tavern", 100),
    ("Basta Pasta", 100),
    ("Blue Smoke", 100),
    ("Crema", 100),
    ("ABC Kitchen", 100),
    ("Almond", 100),
    ("Republic", 100),
    ("Craftbar", 100),
    ("Barn Joo", 100),
    ("Defontes", 100),
    ("Eataly / Park", 100),
    ("Umami", 100),
]

GROUP_NAMES = [
    "Lannister",
    "Targaryen",
    "Stark",
    "Baratheon",
    "Snow",
    "Mormont",
    "Baelish",
    "Cunningham",
    "Seaworth",
    "Greyjoy",
    "Gleeson",
    "Tarly",
    "Clegane",
]
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']
