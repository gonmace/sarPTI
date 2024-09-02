import os
from .base import *
from config.logging import *


DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


ALLOWED_HOSTS = [ "sar.btspti.com", "localhost", "sss.btspti.com" ]

INSTALLED_APPS += [

    ]  

MIDDLEWARE += [
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    ]  

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'base',
        'USER': 'magoreal',
        'PASSWORD': 'ojalaque',
        'HOST': 'sar-db',
        'PORT': '5432',
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'premium175.web-hosting.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True  # Usar SSL en lugar de TLS
EMAIL_HOST_USER = 'admin@btspti.com'
EMAIL_HOST_PASSWORD = 'admin10203040!'
DEFAULT_FROM_EMAIL = 'admin@btspti.com'
