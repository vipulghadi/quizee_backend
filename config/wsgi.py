import os
from dotenv import load_dotenv

print("in WSGI app")
load_dotenv()

# Load environment variables from .env file
load_dotenv()

# Get APP_ENV from environment variables
app_env = os.getenv('APP_ENV', 'local')  # Default to 'local' if APP_ENV is not set

# Set the correct Django settings module based on the environment
if app_env == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
elif (app_env ==
      'dev'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
else:
    # Default to local settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()