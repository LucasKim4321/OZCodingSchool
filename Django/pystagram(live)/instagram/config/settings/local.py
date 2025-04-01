from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instagram',
        'USER': 'dev_user',
        'PASSWORD': 'securepassword',
        'HOST': 'localhost',
        'PORT': '54322',
    }
}


# asgi.py
# manage.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')  # 로컬 환경 셋팅
