import os

from celery import Celery
from django.conf import settings
from kombu import Exchange, Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.project.settings')

app = Celery('core')

app.config_from_object('core.project.celeryconfig', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.task_track_started = True
app.conf.task_ignore_result = False

app.conf.task_queues = (
    Queue('binom_queue', Exchange('binom_queue'), routing_key='binom_queue'),
    Queue('exchange_rates_queue', Exchange('exchange_rates_queue'), routing_key='exchange_rates_queue'),
    Queue('fast_test_queue', Exchange('fast_test_queue'), routing_key='fast_test_queue'),
    Queue('initial_test_queue', Exchange('initial_test_queue'), routing_key='initial_test_queue'),
    Queue('main_test_queue', Exchange('main_test_queue'), routing_key='main_test_queue'),
)

app.conf.task_routes = {
    'core.api.integrations.trackers.tasks.make_limited_api_request': {
        'queue': 'binom_queue',
    },
    'core.api.campaigns.tasks.track_exchange_rates': {
        'queue': 'exchange_rates_queue',
    },
}


@app.on_after_finalize.connect
def trigger_startup_tasks(sender, **kwargs):
    from core.api.campaigns.tasks import track_exchange_rates

    print('Triggering exchange rate task at startup')
    track_exchange_rates.apply_async()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
