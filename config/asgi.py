
import os
from dotenv import load_dotenv

load_dotenv()
app_env = os.getenv('APP_ENV', 'local')

# Set the correct Django settings module based on the environment
if app_env == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
elif app_env == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

from django.core.asgi import get_asgi_application

application = get_asgi_application()