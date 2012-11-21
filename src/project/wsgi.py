# ##PROJECTNAME##
# Copyright (c) 2012 Phil Christensen
#
#
# See LICENSE for details

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
conf.init('/etc/##PROJECTNAME##.yaml', package='##PROJECTNAME##.conf')

import django.core.handlers.wsgi
os.environ['DJANGO_SETTINGS_MODULE'] = '##PROJECTNAME##.settings'
application = django.core.handlers.wsgi.WSGIHandler()
