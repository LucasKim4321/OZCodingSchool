from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "13.124.181.116",  # EC2 퍼블릭 IP
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'instagram',
        'USER': 'dev_user',
        'PASSWORD': 'securepassword',
        'HOST': 'instagram_db',
        'PORT': '5432',
    }
}


# asgi.py
# manage.py
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.prod')  # 배포 환경 셋팅
