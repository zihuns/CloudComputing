# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from cc import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.upload_file, name='upload_file'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)