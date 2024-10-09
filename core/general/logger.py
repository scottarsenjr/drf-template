import json
import logging
from typing import Any, Dict, Optional


class CustomLogger(logging.Logger):
    """
    A custom logger class that extends Python's default logging.Logger with additional
    quality-of-life features, such as structured logging, context injection, and reusable messages.
    """

    def __init__(self, name: str, level=logging.INFO):
        super().__init__(name, level)

    def log_json(self, level: int, message: str, extra: Optional[Dict[str, Any]] = None):
        """
        Log the message in JSON format to make parsing easier for centralized logging tools.
        """
        log_message = {'message': message, 'level': logging.getLevelName(level), 'extra': extra or {}}
        self.log(level, json.dumps(log_message))

    def log_with_context(self, level: int, message: str, context: Dict[str, Any]):
        """
        Log a message along with additional contextual information (e.g., request info, user details).
        """
        formatted_message = f'{message} | Context: {json.dumps(context)}'
        self.log(level, formatted_message)

    def log_retry(self, operation: str, retries: int, max_retries: int):
        """
        Log a message when an operation is retried, with the current retry count and max retries.
        """
        self.info(f'Retrying {operation}. Attempt {retries} of {max_retries}.')

    def log_warning_once(self, message: str, cache: set):
        """
        Log a warning only once by caching the message. This prevents repeated logging of the same warning.
        """
        if message not in cache:
            self.warning(message)
            cache.add(message)

    def log_error(self, error: Exception, context: Optional[Dict[str, Any]] = None):
        """
        Log an error with its associated context (if any) and stack trace.
        """
        error_message = f'Error: {str(error)}'
        if context:
            error_message += f' | Context: {json.dumps(context)}'
        self.error(error_message, exc_info=True)


def get_custom_logger(name: str) -> CustomLogger:
    """
    Factory function to get an instance of the CustomLogger.
    """
    return CustomLogger(name)
