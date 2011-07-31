from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^characters/$', 'characters.views.index'),
    (r'^characters/index$', 'characters.views.index'),
    (r'^characters/bobby$', 'characters.views.index'),
)

