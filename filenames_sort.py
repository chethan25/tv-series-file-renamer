# -*- coding: utf-8 -*-
"""
Module to implement natural sorting
"""
import re
import os


def sorted_alphanumeric(data):
    """Returns sorted filenames"""
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)
