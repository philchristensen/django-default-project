#!/usr/bin/env python

# ##PROJECTNAME##
# Copyright (c) 2012 Phil Christensen
#
#
# See LICENSE for details

import sys, os

from ##PROJECTNAME## import conf

conf.init('/etc/##PROJECTNAME##.yaml', package='##PROJECTNAME##.conf')

# some debug pages use this variable (improperly, imho)
from django.conf import settings
settings.SETTINGS_MODULE = '##PROJECTNAME##.settings'

from django.core import management
u = management.ManagementUtility(sys.argv)
u.execute()