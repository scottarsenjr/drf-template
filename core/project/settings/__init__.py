# Django split settings module for core\project
# https://github.com/sobolevn/django-split-settings

import os.path
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespacing custom env variable
ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(f'{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH', 'local/settings.local.py')

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

# Include settings modules
include(
    'base.py',
    'database.py',
    'security.py',
    'caches.py',
    'logging.py',
    'internationalization.py',
    'rest.py',
    'custom.py',
    'envvars.py',
    'docker.py',
    optional(LOCAL_SETTINGS_PATH),
)
