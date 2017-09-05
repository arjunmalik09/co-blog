"""
Definition of urls for colog.
"""

from datetime import datetime
from django.conf.urls import patterns, url

from django.conf import settings

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^home/', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += patterns(
    'django.views.static',
    (r'media/(?P<path>.*)',
    'serve',
    {'document_root': settings.MEDIA_ROOT}), )