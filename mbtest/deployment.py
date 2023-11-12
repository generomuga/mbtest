import os
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False


# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenose.middleware.WhiteNoiseMiddleWare',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# STATICFILES_STORAGE = 'whitenose.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mssql",
        "NAME": os.getenv('AZURE_SQL_DATABASE'),
        "USER": os.getenv('AZURE_SQL_USER'),
        "PASSWORD": os.getenv('AZURE_SQL_PASSWORD'),
        "HOST": os.getenv('AZURE_SQL_SERVER'),
        "PORT": os.getenv('AZURE_SQL_PORT'), 
    },
},

