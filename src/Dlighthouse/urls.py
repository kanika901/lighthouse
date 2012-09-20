from django.conf.urls.defaults import *
from Dlighthouse import settings
#from Dlighthouse.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# To enable dajaxice
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^Dlighthouse/', include('Dlighthouse.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Go to the login page
    (r'^$', 'django.contrib.auth.views.login'),
    (r'^index/$', 'django.contrib.auth.views.login'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    #  dajaxice URLS
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),

    # For dojango
    #(r'^dojango/', include('dojango.urls')),

    # For Haystack
    #(r'^search/', include('haystack.urls')),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^templates/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.TEMPLATE_ROOT}),
    
    # Link Driver/urls.py for guided, advanced, and keyword Searches.
    (r'^search/', include('Driver.urls')),
    
    # Link registration/backends/default/urls/py for account registration and login/logout.
    (r'^accounts/', include('emailRegistration.urls')),

)
