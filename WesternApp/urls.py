from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WesternApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', "Person.views.homepage"),
    url(r'^signup/', "Person.views.signup"),
    url(r'^logout/', "Person.views.logout_request"),
    url(r'^', "Person.views.intro"),
)
