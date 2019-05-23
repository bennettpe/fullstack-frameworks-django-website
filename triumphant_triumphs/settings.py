"""
Django settings for triumphant_triumphs project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

import os
import dj_database_url

# Used locally and not in Heroku
if os.path.exists('env.py'):
    import env


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: keep the secret key used in production secret!
# A secret key for a particular Django installation
SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
# A boolean that turns on/off debug mode
# Used locally and not in Heroku
if os.path.exists('env.py'):
    DEBUG = True
else:  
    DEBUG = False


# A list of strings representing the host/domain names that this Django site can serve
ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME'),  'fullstack-frameworks-project.herokuapp.com']


# Application definition
# A list of strings designating all applications that are enabled in this Django installation
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'about',
    'accounts',
    'cart',
    'charts',
    'checkout',
    'contact',
    'products',
    'phonenumber_field',
    'storages',
]


# Middleware is a framework of hooks into Django’s request/response processing.
# It’s a light, low-level “plugin” system for globally altering Django’s input or output.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# A string representing the full Python import path to your root URLconf
ROOT_URLCONF = 'triumphant_triumphs.urls'


# Templates
#---------------------------------------------------------------
# A list containing the settings for all template engines to be used with Django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
        },
    },
]


# The full Python path of the WSGI application object that Django’s built-in servers (e.g. runserver) will use
WSGI_APPLICATION = 'triumphant_triumphs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#---------------------------------------------------------------
# Check if DATABASE_URL if not use SQLite3
if "DATABASE_URL" in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print("Database URL not found. Using SQLite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
#------------------------------------------------------------------------------
# The list of validators that are used to check the strength of user’s passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
#----------------------------------------------------
# LANGUAGE_CODE = Represents the name of a language
# USE_I18N      = A boolean that specifies whether Django’s translation system should be enabled
# USE_L10N      = A boolean that specifies if localized formatting of data will be enabled by default or not
# USE_TZ        = A boolean that specifies if datetimes will be timezone-aware by default or not
#----------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#-----------------------------------------------------------
# AWS_DEFAULT_ACL = To stop UserWarning message
# AWS_S3_OBJECT_PARAMETERS = set object parameters on your object
# AWS_STORAGE_BUCKET_NAME = Your Amazon Web Services storage bucket name
# AWS_ACCESS_KEY_ID = Your Amazon Web Services access key
# AWS_SECRET_ACCESS_KEY = Your Amazon Web Services secret access key
# AWS_S3_CUSTOM_DOMAIN =
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}
AWS_DEFAULT_ACL = 'public-read'
AWS_STORAGE_BUCKET_NAME = "pauls-fullstack-frameworks-django-project"
AWS_S3_REGION_NAME = "eu-west-1"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME

# Static files
#-----------------------------------------------------------
# STATIC_ROOT     = Absolute Path to the directory where collectstatic will collect static files for deployment
# STATIC_URL      = URL to use when referring to static files located in STATIC ROOT
# STATICFILES_DIRS = # Look for static files here
# STATICFILES_STORAGE = The file storage engine to use when collecting static files with the collectstatic management command.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    
#STATIC_URL = '/static/'  
STATICFILES_LOCATION = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATICFILES_STORAGE = "custom_storages.StaticStorage"

# Media files
#-----------------------------------------------------------
# MEDIA_URL  = URL that handles media servered from MEDIA_ROOT
# MEDIA_ROOT = Absolute Path to the directory that will hold user-upload files
# Comment out for media hosting in production
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIAFILES_LOCATION = 'media'
#MEDIA_URL = '/media/'  
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)


# Controls where Django stores message data
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"


# Email
#-----------------------------------------------------------
# EMAIL_USE_TLS       = Whether to use a TLS (secure) connection when talking to the SMTP server
# EMAIL_HOST          = The host to use for sending email.
# EMAIL_HOST_USER     = Username to use for the SMTP server defined in EMAIL_HOST
# EMAIL_HOST_PASSWORD = Password to use for the SMTP server defined in EMAIL_HOST
# EMAIL_PORT          = Port to use for the SMTP server defined in EMAIL_HOST.
# EMAIL_BACKEND       = The backend to use for sending emails
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# A list of authentication backend classes (as strings) to use when attempting to authenticate a user
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]


# STRIPE
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')


# PhoneNumberField Django library; allowing the use of GB numbers for contact app
PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'GB'