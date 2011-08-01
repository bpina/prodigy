from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^characters/$', 'characters.views.index'),
    (r'^characters/(?P<character_id>\d+)$', 'characters.views.show'),
    (r'^characters/create/$', 'characters.views.create'),
    (r'^security/login$', 'security.views.login'),
    (r'^security/login/$', 'security.views.login'),
    (r'^$', 'home.views.index'),
    (r'^register/', 'home.views.register')
)

urlpatterns += staticfiles_urlpatterns()
