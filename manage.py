"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv


def main():
    """Run administrative tasks."""

    print("Running administrative tasks")
    load_dotenv()
    app_env = "local"  # Default to 'local' if APP_ENV is not set

    if app_env == 'prod':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')
    elif app_env == 'dev':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()