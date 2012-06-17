#!/usr/bin/env python

# projectname
# Copyright (c) 2012 Phil Christensen
#
#
# See LICENSE for details

import sys, os
from project import conf

conf.init('/etc/project.yaml', package='project.conf')
if __name__ == "__main__":
	# some debug pages use this variable (improperly, imho)
	from django.conf import settings
	settings.SETTINGS_MODULE = 'djunashay.settings'
	
	from django.core.management import execute_from_command_line
	
	execute_from_command_line(sys.argv)

