from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', '##PROJECTNAME##.views.home', name='home'),
	# url(r'^##PROJECTNAME##/', include('##PROJECTNAME##.foo.urls')),

	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	# url(r'^admin/', include(admin.site.urls)),
	# url(r'^assets/', include('##PROJECTNAME##.assets.urls')),
)
