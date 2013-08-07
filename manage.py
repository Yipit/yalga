#!/usr/bin/env python
import os
import sys
from os.path import dirname, abspath, join
LOCAL_FILE = lambda *path: join(abspath(dirname(__file__)), *path)

if __name__ == "__main__":
    sys.path.append(LOCAL_FILE('..'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lunchgameapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
