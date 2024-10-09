import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')  # Default to INFO

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {'()': 'pythonjsonlogger.jsonlogger.JsonFormatter'},
        'verbose': {'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'},
        'simple': {'format': '%(levelname)s %(message)s'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.getenv('LOG_FILE', 'app.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file', 'sentry'],
        'level': LOG_LEVEL,
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file', 'sentry'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'celery': {
            'handlers': ['console', 'file', 'sentry'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}
