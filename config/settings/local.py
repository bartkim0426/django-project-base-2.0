import os

from .partials import *


DEBUG = True

INSTALLED_APPS += [
    # 'debug_toolbar',
    'django_extensions',
]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

INTERNAL_IPS = ['127.0.0.1', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["POSTGRES_DB_NAME"],
        'USER': os.environ["POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(ROOT_DIR + 'db.sqlite3'),
#         # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
