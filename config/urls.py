"""
URL configuration for FacilitaSaúde project.
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('', include('back_end.urls')),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^(?P<path>.*\.css)$', serve, {'document_root': settings.BASE_DIR}),
        re_path(r'^(?P<path>.*\.js)$', serve, {'document_root': settings.BASE_DIR}),
        re_path(r'^(?P<path>.*\.html)$', serve, {'document_root': settings.BASE_DIR}),
        re_path(r'^(?P<path>Imagens/.*)$', serve, {'document_root': settings.BASE_DIR}),
    ]
