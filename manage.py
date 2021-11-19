#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prj_roster.settings")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_roster.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
