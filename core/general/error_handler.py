from functools import wraps

from .logger import get_custom_logger


class GeneralErrorHandler:
    def __init__(self, logger=None, retries=3):
        self.logger = logger or get_custom_logger('general')
        self.retries = retries

    def handle_error(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f'Error in {func.__name__}: {str(e)}')
                return None

        return wrapper
