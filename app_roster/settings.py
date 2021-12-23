"""
Django settings for prj_roster project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import django_heroku


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."

# SECURITY WARNING: don't run with debug turned on in production!

# ★★★herokuから動作させるためいったんfalseに変更★★★
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
#    "hello",
    "app_roster",
    # 'aldjemy',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
#    "django.middleware.csrf.CsrfViewMiddleware", # csrfトークンをいったん削除しておく
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

#ROOT_URLCONF = "prj_roster.urls"
ROOT_URLCONF = "app_roster.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "prj_roster.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE" : "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3")
#     }
# }

# MongoDB
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         # 'ENGINE': 'django.db.backends.',
#         # 'ENGINE': 'django',
#         'ENGINE': 'django_mongodb_engine',
#         'NAME': 'admin',
#         'USER': 'itokita41',
#         'PASSWORD': 'itokita41pass',
#         'HOST': 'cluster0-shard-00-02.tx265.mongodb.net',
#         'PORT': '27017',
#         'SSL': True,
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_mongodb_engine',
#         'NAME': 'rosterdb',
#         'CLIENT': {
#            # 'host': 'mongodb://{user_name}:{pass}@{ip_adress}:{port_num}/{your_dbname}',
#            'host': 'mongodb://itokita41:itokita41pass@cluster0-shard-00-02.tx265.mongodb.net:27107/rosterdb',
#         }
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         "NAME": 'admin',
#         "CLIENT": {
#             'USER': 'itokita41',
#             'PASSWORD': 'itokita41pass',
#             'HOST': 'cluster0-shard-00-02.tx265.mongodb.net',
#             'PORT': '27017',
#             'SSL': True,
# # venv\Lib\site-packages\certifi
#         },
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '[DB名]',                      # Or path to database file if using sqlite3.
        'USER': '[DBユーザ名]',                      # Not used with sqlite3.
        'PASSWORD': '[DBパスワード]',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': 27017,                      # Set to empty string for default. Not used with sqlite3.
    }
}

# mongo cluster0-shard-00-02.tx265.mongodb.net:27017/admin --ssl -u itokita41 -p
# DATABASES= {
#         'default': {
#             'ENGINE': 'djongo',
#             'ENFORCE_SCHEMA': True
#             'NAME': 'your-db-name',
#             'HOST': 'host-name or ip address',
#             'PORT': port_number,
#             'USER': 'db-username',
#             'PASSWORD': 'password',
#             'AUTH_SOURCE': 'db-name',
#             'AUTH_MECHANISM': 'SCRAM-SHA-1',
#             'REPLICASET': 'replicaset',
#             'SSL': 'ssl',
#             'SSL_CERTFILE': 'ssl_certfile',
#             'SSL_CA_CERTS': 'ssl_ca_certs',
#             'READ_PREFERENCE': 'read_preference'
#         }
#     }
# postgresSQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'de5q7mpd4qi77e',
#         'USER': 'rrkwiepojqjmww',
#         'PASSWORD': '172d2d30c807aeca359c780861f63bcaa276bd8b9c25e2e6444ab6b8ec5dbf2c',
#         'HOST': 'ec2-35-172-16-31.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"

django_heroku.settings(locals())
