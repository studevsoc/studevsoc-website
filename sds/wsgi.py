"""
WSGI config for sds project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/sds-dynamic/sds')
sys.path.append('/home/ubuntu/sds-dynamic/env/Lib/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sds.settings")

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sds.settings')

application = get_wsgi_application()
