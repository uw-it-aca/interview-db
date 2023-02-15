from .base_settings import *
import os
from google.oauth2 import service_account

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('ENV', 'prod') == 'localdev'

INSTALLED_APPS.remove('django.contrib.admin')
INSTALLED_APPS += [
    'project.apps.InterviewAdminConfig',
    'interview_db.apps.InterviewConfig',
    'compressor',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':  True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'interview_db.context_processors.google_analytics',
                'interview_db.context_processors.django_debug',
            ],
        }
    }
]

COMPRESS_ROOT = '/static'

COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
    ('text/x-sass', 'pyscss {infile} > {outfile}'),
    ('text/x-scss', 'pyscss {infile} > {outfile}'),
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_OUTPUT_DIR = '/static'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

ADMIN_REORDER = (
    ('app1',('Student','Story')),
    ('app2',('Interview')),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'MEDIA')
MEDIA_URL = '/media/'

if not DEBUG:
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
        '/gcs/credentials.json')
    GS_CACHE_CONTROL = 'public, max-age=604800'
    GS_DEFAULT_ACL = 'publicRead'

INTERVIEW_DB_AUTHZ_GROUPS = {
    'admin': os.getenv("ID_ADMIN_GROUP", 'u_test_admin'),
    'front-end': os.getenv("ID_FRONT_END_GROUP", 'u_test_front_end'),
}

if os.getenv('AUTH', 'NONE') == 'SAML_MOCK':
    MOCK_SAML_ATTRIBUTES['isMemberOf'] = [
        INTERVIEW_DB_AUTHZ_GROUPS['admin'],
        INTERVIEW_DB_AUTHZ_GROUPS['front-end'],
    ]
