from .base_settings import *
import os
from google.oauth2 import service_account

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('ENV', 'localdev') == 'localdev'

INSTALLED_APPS.remove('django.contrib.admin')
INSTALLED_APPS += [
    'project.apps.InterviewAdminConfig',
    'interview_db.apps.InterviewConfig',
    'rest_framework',
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

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_REORDER = (
    ('app1', ('Student', 'Story')),
    ('app2', 'Interview'),
)

INTERVIEW_DB_AUTHZ_GROUPS = {
    'admin': os.getenv('ID_ADMIN_GROUP', 'u_test_admin'),
    'front-end': os.getenv('ID_FRONT_END_GROUP', 'u_test_front_end'),
}

if os.getenv('AUTH', 'NONE') == 'SAML_MOCK':
    MOCK_SAML_ATTRIBUTES['isMemberOf'] = [
        INTERVIEW_DB_AUTHZ_GROUPS['admin'],
        INTERVIEW_DB_AUTHZ_GROUPS['front-end'],
    ]

if os.getenv('ENV', 'localdev') == 'localdev':
    MEDIA_ROOT = os.getenv('MEDIA_ROOT', '/app/media')
    VITE_MANIFEST_PATH = os.path.join(
        BASE_DIR, 'interview_db', 'static', 'manifest.json'
    )
else:
    STORAGES = {
        'default': {
            'BACKEND': 'storages.backends.gcloud.GoogleCloudStorage',
            'OPTIONS': {
                'project_id': os.getenv('STORAGE_PROJECT_ID', ''),
                'bucket_name': os.getenv('STORAGE_BUCKET_NAME', ''),
                'location': os.path.join(os.getenv('STORAGE_DATA_ROOT', '')),
                'credentials': service_account.Credentials.
                from_service_account_file(
                    '/gcs/credentials.json'),
            }
        },
        'staticfiles': {
            'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
        },
    }
    VITE_MANIFEST_PATH = os.path.join(os.sep, 'static', 'manifest.json')
    CSRF_TRUSTED_ORIGINS = ['https://' + os.getenv('CLUSTER_CNAME')]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PAGINATION_CLASS': [
        'rest_framework.pagination.PageNumberPagination',
    ],
    'PAGE_SIZE': 10,
}

IMAGE_CACHE_EXPIRES = 60 * 60
