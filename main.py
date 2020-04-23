# -*- coding: utf-8 -*-
"""
Module to accept pathname and tv series name from command line arguments
"""
import os
import sys


try:
    # Store file path and tv series name using command line arguments
    path = sys.argv[1]
    tv_series_name = sys.argv[2]
except IndexError:
    raise SystemExit('Path or tv series name not given')
else:
    try:
        os.listdir(path)
    except FileNotFoundError:
        raise SystemExit('Invalid path')
    else:
        # Importing rename module here to avoid circular dependencies
        import rename
