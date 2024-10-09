from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'track-exchange-rates-every-day': {
        'task': 'core.api.campaigns.tasks.track_exchange_rates',
        'schedule': crontab(hour='0', minute='0'),
    },
    'run-fast-test-constructor': {
        'task': 'core.api.testers.tasks.run_constructor',
        'schedule': crontab(minute='*/17'),
        'args': ('fast_test_constructor',),
        'options': {
            'queue': 'fast_test_queue',
        },
    },
    'run-initial-test-constructor': {
        'task': 'core.api.testers.tasks.run_constructor',
        'schedule': crontab(hour='*/1', minute='40'),
        'args': ('initial_test_constructor',),
        'options': {
            'queue': 'initial_test_queue',
        },
    },
    'run-main-test-constructor': {
        'task': 'core.api.testers.tasks.run_constructor',
        'schedule': crontab(hour='*/6', minute='5'),
        'args': ('main_test_constructor',),
        'options': {
            'queue': 'main_test_queue',
        },
    },
}
