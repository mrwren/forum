from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^register/', 'forum.views.register'),
	url(r'^login/', 'forum.views.login'),
	url(r'^logout/', 'forum.views.logout'),
	url(r'^forum/', 'forum.views.forum'), 
	url(r'^admin/', include(admin.site.urls)),
)
