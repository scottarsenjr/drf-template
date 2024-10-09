ifeq ($(OS),Windows_NT)
    MANAGE_PY := poetry run python -m core.manage
    COPY_CMD := python -c "import shutil; shutil.copyfile('./core/project/settings/templates/settings.local.py', './local/settings.local.py'); shutil.copyfile('./core/project/settings/templates/settings.prod.py', './local/settings.prod.py')"
else
    MANAGE_PY := poetry run python3.11 -m core.manage
    COPY_CMD := python3 -c "import shutil; shutil.copyfile('./core/project/settings/templates/settings.local.py', './local/settings.local.py'); shutil.copyfile('./core/project/settings/templates/settings.prod.py', './local/settings.prod.py')"
endif

# Project Setup/Managing commands
.PHONY: install
install:
	poetry install

.PHONY: copy-template
copy-template:
	$(COPY_CMD)

.PHONY: pre-commit-uninstall
pre-commit-uninstall:
	poetry run pre-commit uninstall

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

.PHONY: install-pre-commit
update-pre-commit: pre-commit-uninstall pre-commit-install;

.PHONY: migrate
migrate:
	poetry run $(MANAGE_PY) migrate

.PHONY: migrations
migrations:
	poetry run $(MANAGE_PY) makemigrations

.PHONY: superuser
superuser:
	poetry run $(MANAGE_PY) createsuperuser

.PHONY: run-server
run-server:
	poetry run $(MANAGE_PY) runserver

.PHONY: run-celery
run-celery:
	poetry run celery -A core.project worker --loglevel=debug --pool=solo

.PHONY: run-flower
run-flower:
	poetry run celery flower --port=5000

.PHONY: run-celery-beat
run-celery-beat:
	poetry run celery -A core.project beat --loglevel=debug

.PHONY: update
update:
	install migrate update-pre-commit

.PHONY: lint
lint:
	poetry run pre-commit run --all-files
	poetry run ruff check .

.PHONY: build-prod-container
build-prod-container:
	docker compose --env-file .env.prod up --build -d

.PHONY: prod-container-up
prod-container-up:
	docker compose --env-file .env.prod up

# Prevent make from interpreting the argument as a make target
%:
	@:
