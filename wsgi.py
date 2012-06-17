# projectname
# Copyright (c) 2012 Phil Christensen
#
#
# See LICENSE for details

"""
WSGI config for djunashay project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
# import sys
# # remove system site-packages and dist-packages dirs
# sys.path = [x for x in sys.path if 'site-packages' not in x and 'dist-packages' not in x]
# 
# # add the virtualenv site-packages to the PYTHONPATH
# import site
# site.addsitedir('/srv/example.com/virtualenv/lib/python2.6/site-packages')

import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp'

from fuwt_common import conf
conf.init('/etc/project.yaml', package='project.conf')

import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
