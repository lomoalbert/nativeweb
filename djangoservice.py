#!/usr/bin/env python
__author__ = 'way'


import os
from django.core.management import execute_from_command_line

def djangoserver(argv):
    print djangoserver
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
    execute_from_command_line(argv)

