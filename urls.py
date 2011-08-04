from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^characters/$', 'characters.views.index'),
    (r'^characters/(?P<server_name>\w+)/(?P<character_name>\w+)/$', 'characters.views.show'),
    (r'^characters/create/$', 'characters.views.create'),
    (r'^characters/update/$', 'characters.views.update'),
    (r'^security/login$', 'security.views.login'),
    (r'^security/login/$', 'security.views.login'),
    (r'^security/logout/$', 'security.views.logout'),
    (r'^$', 'home.views.index'),
    (r'^register/', 'home.views.register'),
    (r'^user/$', 'users.views.index'),
    (r'^user/select_default_character/', 'users.views.select_default_character'),
    (r'^guilds/create/', 'guilds.views.create'),
    (r'^guilds/(?P<server_name>\w+)/(?P<guild_name>[\w|\W]+)/$', 'guilds.views.show'),
    (r'^servers/(?P<server_name>\w+)/$', 'servers.views.show'),
)

urlpatterns += staticfiles_urlpatterns()
