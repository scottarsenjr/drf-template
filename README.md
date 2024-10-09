# Template for DRF, PostgreSQL and JWT Authentication project

## Quick Installation

Create virtual environment with
```shell
python -m venv .venv
```

Install poetry
```shell
pip install poetry
```

Install dependencies
```shell
poetry install
```

Copy local settings
```shell
make copy-template
```

## Run development server

Start development server
```shell
make run-server
```

Optional: Run Celery
```shell
make run-celery
```

Optional: Run Celery beat
```shell
make run-celery-beat
```

## Run production server

Build docker container
```shell
make build-prod-container
```

Run docker container
```shell
make prod-container-up
```
