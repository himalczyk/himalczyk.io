"""
Django settings for portfolio_blog project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING settings
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_SECONDS = 3600
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ["https://*.herokuapp.com", "https://himalczyk.herokuapp.com/"]
ALLOWED_HOSTS = ["himalczyk.io", "https://himalczyk.io", "", "*"]
# dev
# SECRET_KEY = os.getenv("SECRET_KEY_DEV")
# DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "theme",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "tailwind",
    "django_browser_reload",
    "portfolio",
    "tutorial",
    "followed_sources",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "portfolio_blog.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio_blog.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "staticfiles/"
STATICFILES_DIRS = [BASE_DIR / "static", BASE_DIR / "media"]
STATIC_ROOT = BASE_DIR / "staticfiles"
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
# WHITENOISE_USE_FINDERS = True
# WHITENOISE_MANIFEST_STRICT = False
# WHITENOISE_ALLOW_ALL_ORIGINS = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]

TAILWIND_CSS_PATH = "css/dist/styles.css"

# this is fixing the pathing issue for being able to find node installed on pc and heroku
# DEV
# NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
# PROD
NPM_BIN_PATH = "/app/.heroku/node/bin/npm"
# linux
# NPM_BIN_PATH = "/usr/local/bin/npm"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                + "pathname=%(pathname)s lineno=%(lineno)s "
                + "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "testlogger": {
            "handlers": ["console"],
            "level": "INFO",
        }
    },
}

import django_on_heroku

django_on_heroku.settings(locals())
