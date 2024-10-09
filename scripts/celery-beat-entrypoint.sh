#!/usr/bin/env bash

set -e

echo 'Starting Celery beat...'
poetry run celery -A core.project beat -l info
