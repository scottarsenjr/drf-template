#!/usr/bin/env bash

set -e

echo 'Starting Celery worker...'
poetry run celery -A core.project worker -l info -P solo
