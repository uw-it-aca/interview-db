from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

from interview_db.admin import saml_admin_site

from .base_urls import *

urlpatterns += [
    path("admin/", saml_admin_site.urls),
    re_path(r"^", include("interview_db.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
