from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from .base_urls import *

urlpatterns += [
    url('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^', include('interview_db.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
