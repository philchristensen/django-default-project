#!/usr/bin/env python

# projectname
# Copyright (c) 2012 Phil Christensen
#
#
# See LICENSE for details

import sys, os

from project import conf

conf.init('/etc/project.yaml', package='project.conf')

# some debug pages use this variable (improperly, imho)
from django.conf import settings
settings.SETTINGS_MODULE = 'project.settings'

from django.core import management
u = management.ManagementUtility(sys.argv)
u.execute()