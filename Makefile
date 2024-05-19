APP_PATH := portfolio_blog
PYTHON := python3
DJANGO_MANAGE := $(PYTHON) manage.py

# Default target
.PHONY: all
all: server tailwind

# Run Django development server
.PHONY: server
server:
	cd $(APP_PATH) && $(DJANGO_MANAGE) runserver

# Run Tailwind CSS watcher
.PHONY: tailwind
tailwind:
	cd $(APP_PATH) && $(DJANGO_MANAGE) tailwind start
