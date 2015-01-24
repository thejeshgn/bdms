from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url('^$',home, name='home'),
    url(r'^bdms-admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
)
#urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',(r'^pages/', include('django.contrib.flatpages.urls')),)
urlpatterns += patterns('django.contrib.flatpages.views',)

urlpatterns += patterns('',(r'^users/', include('password_reset.urls') ),)



if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

