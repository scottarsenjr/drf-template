# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /opt/project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH ./
ENV CORESETTINGS_IN_DOCKER true

# Install dependencies
RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==1.4.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

# Copy project files
COPY ["README.md", "Makefile", "./"]
COPY core core
COPY local local
COPY scripts scripts

# Expose the Django development server port (adjust if needed)
EXPOSE 8000

# Set up the entrypoints
RUN chmod a+x ./scripts/entrypoint.sh ./scripts/celery-entrypoint.sh ./scripts/celery-beat-entrypoint.sh

ENTRYPOINT ["./scripts/entrypoint.sh"]
