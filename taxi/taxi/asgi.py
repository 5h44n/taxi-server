# taxi/asgi.py

import os
import django

from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')
django.setup()
applicaiton = get_default_application()
