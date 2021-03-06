#!/usr/bin/env python

# КОНСОЛЬ:
# git add --all; git commit -m "Сохранение"; git push -u origin master; ssh j1100207@j1100207.myjino.ru; 
# cd projects/demo/shop_of_socks; git pull;

import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
