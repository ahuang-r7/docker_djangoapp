"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

os.environ['TCELL_AGENT_CONFIG'] = '/Users/ahuang/Desktop/docker_djangoapp/root/tcell/tcell_agent.config'
os.environ['TCELL_AGENT_HOME'] = '/Users/ahuang/Desktop/docker_djangoapp/root/tcell'

import tcell_agent

tcell_agent.init()

application = get_wsgi_application()
