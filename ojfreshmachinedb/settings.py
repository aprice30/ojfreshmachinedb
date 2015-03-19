"""
Django settings for ojfreshmachinedb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# TODO: This seems very dirty. Is there a better way?
if (os.environ.get('DEBUG') != None):
    import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY','8u+r78k0#)@ucu4^$ye1ig7nygllic!vod!1zlwg7_$2l=@6ho')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get('DEBUG') != None else False

TEMPLATE_DEBUG = True if os.environ.get('DEBUG') != None else False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'company',
    'machine'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ojfreshmachinedb.urls'

WSGI_APPLICATION = 'ojfreshmachinedb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-db'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# TODO: Seems dirty. Can we do better?
# If we are not running locally, fetch database details from heroku
if (os.environ.get('DEBUG') != None):
    # Parse database configuration from $DATABASE_URL
    DATABASES['default'] =  dj_database_url.config()

    # Enable Connection Pooling (if desired)
    DATABASES['default']['ENGINE'] = 'django_postgrespool'

    # Honor the 'X-Forwarded-Proto' header for request.is_secure()
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # Allow all host headers
    ALLOWED_HOSTS = ['*']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = 'https://aprice30.github.io/ojfreshmachinedb/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
