"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') # 셋팅 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # 로컬 환경 셋팅
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')  # 로컬 환경 셋팅

application = get_wsgi_application()
