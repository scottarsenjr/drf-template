from core.general.utils.collections import deep_update
from core.general.utils.settings import get_settings_from_env

# Takes ENV variables with a matching prefix, strips it out, then adds it to the globals
#
# EXAMPLE USAGE:
# `export CORESETTINGS_IN_DOCKER=true` (env variable)
#
# Could then be referenced as a global as:
# `IN_DOCKER` (where the value would be `True`)

deep_update(globals(), get_settings_from_env(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa:F821
