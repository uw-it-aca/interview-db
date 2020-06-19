from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include, reverse_lazy

from .base_urls import *

from interview_db.views import site

urlpatterns += [
    path('admin/', site.urls),
    re_path(r'^', include('interview_db.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
