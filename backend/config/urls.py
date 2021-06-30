from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.documentation import include_docs_urls

from .routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("api/__debug__/", include(debug_toolbar.urls))] + urlpatterns
