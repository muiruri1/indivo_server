import os

# settings.py:
#
# Settings for the IndivoX Backend Server.

###############################
# For Instance Administrators #
###############################

# Required Setup #
##################

# People who will get emailed when errors are raised
# See https://docs.djangoproject.com/en/1.2/howto/error-reporting/
# Use tuples of ('Full Name', 'email'), i.e.
# ADMINS = (
#    ('John Doe', 'jdoe@gmail.com'),
# )
ADMINS = (
    )

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'REPLACEMENOW'

# absolute filepath where indivo_server is installed
APP_HOME = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)

# Automatically create new records with sample data by default
DEMO_MODE = False

# which sample data to load when in demo mode. Maps desired record labels
# to data profiles. 'Data profiles' correspond
# to subfolders of SAMPLE_DATA_DIR
DEMO_PROFILES = {
    'William Robinson':'patient_967332',
    }

# Location for sample data
SAMPLE_DATA_DIR = APP_HOME + '/sample_data'

# URL prefix (where indivo_server will be accessible from the web)
SITE_URL_PREFIX = "http://localhost:8000"

# Description to show in SMART manifest call
SITE_DESCRIPTION = "Indivo Server"

# URL prefix for the UI server
# (usually port 80 on the same machine)
UI_SERVER_URL = 'http://localhost'

# Storage Settings
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2', # '.postgresql_psycopg2', '.mysql', or '.oracle'
        'NAME':'indivo', # Required to be non-empty string
        'USER':'', # Required to be non-empty string
        'PASSWORD':'',
        'HOST':'', # Set to empty string for localhost.
        'PORT':'', # Set to empty string for default.
        },
}

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# In Indivo, all binary documents (pdf, etc.) are stored as files in MEDIA_ROOT
# This storage could potentially grow large, so pick this location accordingly
MEDIA_ROOT = APP_HOME + '/indivo_files/'

# Email settings
SEND_MAIL = False # Turn email on at all?
EMAIL_HOST = ""
EMAIL_PORT = 25
EMAIL_FROM_ADDRESS = "Indivo <support@indivo.localhost>"
EMAIL_SUPPORT_ADDRESS = "support@indivo.localhost"
EMAIL_SUPPORT_NAME = "Indivo Support"

# Timeout before reenabling a disabled account
# in seconds. None if you don't want reenabling.
# Accounts are disabled after 3 consecutive failed
# logins.
ACCOUNT_REENABLE_TIMEOUT = None

# Advanced Setup #
##################

# Default carenets for new records
INDIVO_DEFAULT_CARENETS = ['Family', 'Physicians', 'Work/School']

# Audit Settings
AUDIT_LEVEL = 'HIGH' # 'HIGH', 'MED', 'LOW', 'NONE'
AUDIT_OAUTH = True # Audit the calls used solely for the oauth dance?
AUDIT_FAILURE = True # Audit the calls that return with unsuccessful status (4XX, 5XX)?

# Apps Settings
APPS_DIRS = {
    'ui': [APP_HOME + '/registered_apps/ui',],
    'admin': [APP_HOME + '/registered_apps/admin',],
    'user': [APP_HOME + '/registered_apps/user',],
}

# DataModel Settings
CORE_DATAMODEL_DIRS = [APP_HOME + '/indivo/data_models/core',] # Directories for core datamodel definitions
CONTRIB_DATAMODEL_DIRS = [APP_HOME + '/indivo/data_models/contrib',] # Directories for contributed datamodel definitions

# XML Validation and Transformation settings
VALIDATE_XML_SYNTAX = True # Validate all incoming XML docs for basic syntax?
VALIDATE_XML = True # Validate XML docs to process against the Indivo schemas?
CORE_SCHEMA_DIRS = [APP_HOME + '/indivo/schemas/data/core',] # Directories for core schemas
CONTRIB_SCHEMA_DIRS = [APP_HOME + '/indivo/schemas/data/contrib',] # Directories for contributed schemas

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(APP_HOME, 'indivo.log'),
            },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': False,
            'level':'INFO',
            },
        'django.db.backends': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
            },
        'oauth': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'south': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'indivo': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

#############################
# For Indivo/Django Experts #
#############################

# excluse a URL pattern from access control
INDIVO_ACCESS_CONTROL_EXCEPTION = "^/codes/"

MANAGERS = ADMINS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.

## IMPORTANT for Indivo: do NOT change this timezone to your local timezone.
## KEEP IT as UTC.
TIME_ZONE = 'UTC'
USE_TZ = True
## ALSO, we recommend that, if you use PostgreSQL, you set the timezone to UTC in postgresql.conf

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'indivo.middlewares.authentication.Authentication',
    'indivo.middlewares.paramloader.ParamLoader',
    'indivo.middlewares.authorization.Authorization',
    'indivo.middlewares.audit.AuditWrapper'
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
  APP_HOME + "/templates",
  APP_HOME + "/indivo/templates"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'indivo',
    'codingsystems',
    'south',  # for migrations
)

# cookie
SESSION_COOKIE_NAME = "indivo_server_sessionid"

# auth
LOGIN_URL = "/account/login"

# no trailing slash just because
APPEND_SLASH = False

# custom serializations
SERIALIZATION_MODULES = {
    "indivo_python" : "indivo.serializers.python",
    "indivo_xml": "indivo.serializers.xml_serializer"
}


DATETIME_INPUT_FORMATS = (
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
    "%Y-%m-%dT%H:%M:%S.%fZ", #ISO8601_UTC_DATETIME_FORMAT_MICRO
    "%Y-%m-%dT%H:%M:%SZ",    #ISO8601_UTC_DATETIME_FORMAT
)

STATIC_URL = '/static/'
