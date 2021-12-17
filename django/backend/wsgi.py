"""
Script file: wsgi.py
Created on: Feb 25, 2021
Last modified on: Mar 28, 2021

Comments:
    WSGI config for backend project.
    It exposes the WSGI callable as a module-level variable named `application`.
    For more information on this file, see
    https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.docker')
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings.docker'
application = get_wsgi_application()
