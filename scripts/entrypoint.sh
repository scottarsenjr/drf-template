#!/usr/bin/env bash

set -e

RUN_MANAGE_PY='poetry run python3.11 -m core.manage'

echo 'Collecting static files...'
$RUN_MANAGE_PY collectstatic --no-input

echo 'Running migrations...'
$RUN_MANAGE_PY migrate --no-input

poetry run gunicorn --bind 0.0.0.0:8000 core.project.asgi -w 4 -k uvicorn.workers.UvicornWorker
