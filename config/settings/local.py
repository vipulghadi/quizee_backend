from .base import *

print("in local Settings")
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-api-key',
)

CSRF_TRUSTED_ORIGINS = []

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT"
    ]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': os.getenv('LOCAL_DB_NAME'),
    #     'USER': os.getenv('LOCAL_DB_USER'),
    #     'PASSWORD': os.getenv('LOCAL_DB_PASSWORD'),
    #     'HOST': os.getenv('LOCAL_DB_HOST'),
    #     'PORT': os.getenv('LOCAL_DB_PORT'),
    # }
}
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'
