"""
Definition of urls for WebAnalytics.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^dashboard/$',app.views.dashboard, name='dashboard'),
    url(r'^dashboard$',app.views.dashboard, name='dashboard'),
    url(r'^segmentation$',app.views.segmentation, name='segmentation'),
    url(r'^login$',app.views.login, name='login')
        

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
