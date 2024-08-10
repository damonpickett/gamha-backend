"""
WSGI config for gamha_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gamha_blog.settings")

application = get_wsgi_application()
BASE_DIR = settings.BASE_DIR
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))
