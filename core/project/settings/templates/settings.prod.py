import os
from pathlib import Path

from dotenv import load_dotenv

worker_pid = os.getpid()

dotenv_path = Path.joinpath(Path(__file__).parent.parent.parent.parent.resolve(), '.env.prod')

print(
    'Loading ENV variables from {env_path} for worker with PID: {worker_pid}'.format(
        env_path=dotenv_path, worker_pid=worker_pid
    )
)

load_dotenv(dotenv_path)

PROTOCOL = os.environ.get('PROTOCOL', 'http')
DOMAIN = os.environ.get('DOMAIN', 'localhost')

DEBUG = True
SECRET_KEY = 'django-insecure-=okvqjswarmd2ymc#jxqo-t7a(9qpvk-dk8v#9$t^c(dlbmw)b'

STATIC_ROOT = '/opt/project/static/'
MEDIA_ROOT = '/opt/project/media/'

MEDIA_URL = f'{PROTOCOL}://{DOMAIN}/media/'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://cache:6379/0',
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'},
    },
    'celery_broker': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://cache:6379/1',
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'},
    },
    'celery_cache_backend': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://cache:6379/2',
        'OPTIONS': {'CLIENT_CLASS': 'django_redis.client.DefaultClient'},
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 600,
    }
}

print('Local settings have been exported for worker {worker_pid}'.format(worker_pid=worker_pid))
