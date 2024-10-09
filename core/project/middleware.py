import traceback

from django.conf import settings
from core.general.logger import get_custom_logger

logger = get_custom_logger('django')


class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            logger.error('Exception occurred: %s', traceback.format_exc())
