"""WSGI config for {{ project_name }} project."""
import os

# Add the app code to the path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../")
sys.path.append(PROJECT_ROOT)

# set environment variable
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{ project_name }}.settings"
)

# This application object is used by any WSGI server configured to use
# this file. This includes Django's development server, if the
# WSGI_APPLICATION setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

