# coding=utf-8
# Django settings for requery project.
import os
PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# BANCO_CAVEIRAO = {
#     'ENGINE': 'django.db.backends.mysql', 'PORT': '3306',
#     'USER': 'implantacao', 'PASSWORD': 'KTTYQea6', 'HOST': '192.168.1.105',
# }
# BASE_SIEVE = dict({'NAME' : 'sieve'}, **BANCO_CAVEIRAO)
#
# BANCO_ORACULO = {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'HOST': 'db0.sieve.com.br',
#     'USER': 'usr_jleite',
#     'PASSWORD': 'sievera',
#     'OPTIONS': {'autocommit': True, }
# }
#
# DATABASES = {
#     'default': dict({'NAME' : 'django_control'}, **BANCO_CAVEIRAO),
#     'manager': dict({'NAME' : 'webetl_manager'}, **BANCO_CAVEIRAO),
#     'portal':BASE_SIEVE,
#     'api_portal':BASE_SIEVE,
#     'crm': BASE_SIEVE,
#     'operation': BASE_SIEVE,
#     'finance': BASE_SIEVE,
#     # 'matching': dict({'NAME' : 'matching_prod'}, **BANCO_CAVEIRAO),
#     'jobs': dict({'NAME' : 'sievejobs'}, **BANCO_CAVEIRAO),
#     'baseproduto': dict({'NAME' : 'baseproduto'}, **BANCO_CAVEIRAO),
#     'buscadescontos': dict({'NAME': 'buscadescontos'}, **BANCO_CAVEIRAO),
#     'matching': dict({'NAME': 'matching'}, **BANCO_ORACULO)
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'django_control',                      # Or path to database file if using sqlite3.
        'USER': 'sievedb',                      # Not used with sqlite3.
        'PASSWORD': '93849sieve',                  # Not used with sqlite3.
        'HOST': '208.101.8.67',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'helpdesk': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': "sieve",
        'USER': "django_prod",
        'PASSWORD': "vzmwZrY7",
        'HOST': "dumbo.sieve.com.br",
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'manager': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'webetl_manager',                      # Or path to database file if using sqlite3.
        'USER': 'django',                      # Not used with sqlite3.
        'PASSWORD': 'XR762OQ=',                  # Not used with sqlite3.
        'HOST': 'webetlmanager.sieve.com.br',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'portal': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': "sieve",
        'USER': "django_prod",
        'PASSWORD': "vzmwZrY7",
        'HOST': "dumbo.sieve.com.br",
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'portal_slave': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sieve',                      # Or path to database file if using sqlite3.
        'USER': 'django_prod',                      # Not used with sqlite3.
        'PASSWORD': 'vzmwZrY7',                  # Not used with sqlite3.
        'HOST': 'dumbo.slave.sieve.com.br',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'finance': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': "sieve",
        'USER': "django_prod",
        'PASSWORD': "vzmwZrY7",
        'HOST': "dumbo.sieve.com.br",
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'api_portal': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': "sieve",
        'USER': "django_prod",
        'PASSWORD': "vzmwZrY7",
        'HOST': "dumbo.sieve.com.br",
        'PORT': '',
    },
    'crm': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "sieve",
        'USER': "django_prod",
        'PASSWORD': "vzmwZrY7",
        'HOST': "dumbo.sieve.com.br",
        'PORT': '',
    },
    'operation': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "sieve",
        'USER': "django_prod",
        'PASSWORD': "vzmwZrY7",
        'HOST': "dumbo.sieve.com.br",
        'PORT': '',
    },
    'old_jobs': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sievejobs',                      # Or path to database file if using sqlite3.
        'USER': 'sievedb',                      # Not used with sqlite3.
        'PASSWORD': '93849sieve',                  # Not used with sqlite3.
        'HOST': 'jetranger.sieve.com.br',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'minuano': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'minuano',                      # Or path to database file if using sqlite3.
        'USER': 'sievedb',                      # Not used with sqlite3.
        'PASSWORD': '93849sieve',                  # Not used with sqlite3.
        'HOST': 'jetranger.sieve.com.br',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'jobs': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': "sievejobs",
        'USER': "django",
        'PASSWORD': "Hlr7ZA",
        'HOST': "dumbo.jobs.webetl.com.br",
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'baseproduto': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'baseproduto',
            'USER': 'django',
            'PASSWORD': 'XR762OQ=',
            'HOST': '173.193.20.243',
            'PORT': '',
    },
    'bi_pentaho': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pentaho_repository',
            'USER': 'django',
            'PASSWORD': '7sCzcazY',
            'HOST': 'bi.sieve.com.br',
            'PORT': '',
    },
    'bi_cubo': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bi_dm1',
            'USER': 'django',
            'PASSWORD': '7sCzcazY',
            'HOST': 'bi.sieve.com.br',
            'PORT': '',
    },
    'zendesk': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'zendesk',
            'USER': 'django',
            'PASSWORD': '7sCzcazY',
            'HOST': 'bi.sieve.com.br',
            'PORT': '',
    },
    'oraculo': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'oraculo',
            'USER': 'django',
            'PASSWORD': 'XR762OQ=',
            'HOST': 'oraculo.sieve.com.br',
            'PORT': '',
    },
    'matching': {
        'NAME': 'matching',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': "dumbo.oraculo.sieve.com.br",
        'USER': 'matching',
        'PASSWORD': '#dev@sieve5',
    },
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

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
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    #PROJECT_DIR + "/requery/static/",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!+1d_2fb299fa^jjhr7)lfrnwe2*(@rqc@r9oe5&amp;71e53i=%0^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.templates.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    )

ROOT_URLCONF = 'project_requery.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project_requery.wsgi.application'

TEMPLATE_DIRS = ()

INSTALLED_APPS = (
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
    'requery',
)

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
