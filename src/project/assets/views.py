# ##PROJECTNAME##
# Copyright (c) 2012 Phil Christensen
#
#
# See LICENSE for details

"""
Django view for serving static assets via XSendfile
"""

import os, posixpath, urllib

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import Http404
from django.views import static
from django.contrib.staticfiles import finders

def serve_static(request, path, document_root=None, **kwargs):
	"""
	Serve static files below a given point in the directory structure or
	from locations inferred from the staticfiles finders.

	Instead of raising an error when serving static files in DEBUG mode,
	this view adds an X-Sendfile header.
	"""
	if not settings.DEBUG and not settings.XSENDFILE:
		raise ImproperlyConfigured("The staticfiles view can only be used in "
								   "debug mode or when X-Sendfiles is active.")
	
	normalized_path = posixpath.normpath(urllib.unquote(path)).lstrip('/')
	absolute_path = finders.find(normalized_path)
	if not absolute_path:
		raise Http404("'%s' could not be found" % path)
	
	document_root, path = os.path.split(absolute_path)
	response = static.serve(request, path, document_root=document_root, **kwargs)

	if(settings.XSENDFILE):
		response._container = ['']
		response["X-Sendfile"] = absolute_path
	
	return response
