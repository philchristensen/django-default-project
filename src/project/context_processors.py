# antioch
# Copyright (c) 1999-2012 Phil Christensen
#
#
# See LICENSE for details

"""
Add some essential variables to the template environment.
"""

from django.conf import settings

from antioch import assets

def default_variables(request):
	"""
	Adds default context variables to the template.
	"""
	return {
		'BOOTSTRAP_MEDIA': assets.LessMedia(
			css         = dict(
				screen  = [
					'%sbootstrap/docs/assets/css/bootstrap.css' % settings.STATIC_URL,
					'%sbootstrap/docs/assets/css/bootstrap-responsive.css' % settings.STATIC_URL,
				],
			),
		),
	}

