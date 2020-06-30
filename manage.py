#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def handleKill(signum, frame):
    print ("Killing Thread.")
    # Or whatever code you want here
    ForceTerminate.FORCE_TERMINATE = True 
    print (threading.active_count())
    exit(0)


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nbody_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    signal.signal(signal.SIGINT, handleKill)
    signal.signal(signal.SIGTERM, handleKill)
    execute_from_command_line(sys.argv)

"""

if __name__ == '__main__':
    main()

"""


from django.core.management import execute_from_command_line
import signal
import threading

"""
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    signal.signal(signal.SIGINT, handleKill)
    signal.signal(signal.SIGTERM, handleKill)
    
    execute_from_command_line(sys.argv)
"""
