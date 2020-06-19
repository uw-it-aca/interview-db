from django.contrib.admin.apps import AdminConfig

class SAMLAdminConfig(AdminConfig):
    default_site = 'interview_db.admin.SAMLAdminSite'