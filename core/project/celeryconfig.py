from django.conf import settings

from core.project.celery.tasks import CELERY_BEAT_SCHEDULE  # noqa:F401

# CELERY SETTINGS
broker_url = settings.CELERY_BROKER_URL
result_backend = settings.CELERY_RESULT_BACKEND

cache_backend = (
    settings.CACHES['celery_cache_backend']['LOCATION']
    if 'celery_cache_backend' in settings.CACHES
    else 'redis://localhost:6379/2'
)

accept_content = ['application/json']
task_serializer = 'json'
result_serializer = 'json'
timezone = 'Europe/Moscow'
result_persistent = True
worker_hijack_root_logger = False
