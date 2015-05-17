# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from views import ThreadListView

urlpatterns = [
    url(r'^threads/$', ThreadListView.as_view(template_name='app_main/threads.html'), name="threads"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)