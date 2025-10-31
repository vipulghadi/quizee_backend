from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


API_VERSION = settings.API_VERSION
urlpatterns = [

    path('god/', admin.site.urls),
    path(f'api/{API_VERSION}/auth/', include('apps.authentication.urls.client')),
    path(f'api/{API_VERSION}/admin/auth/', include('apps.authentication.urls.admin')),

    path(f'api/{API_VERSION}/account/', include('apps.account.urls.client')),
    path(f'api/{API_VERSION}/admin/questionbank/', include('apps.questionbank.urls.admin')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)