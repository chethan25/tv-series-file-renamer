#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to rename the files
"""
import os
import sys

import scraper
from rename import sorted_alphanumeric

new_episode_list = scraper.episode_list

try:
    # Store file path using command line arguments
    path = sys.argv[1]
except IndexError:
    raise SystemExit('Path not given')
else:
    try:
        os.listdir(path)
    except FileNotFoundError:
        raise SystemExit('Invalid path')
    else:
        episode = 0
        for episode_name in sorted_alphanumeric(os.listdir(path)):
            # Assign src with files path name
            src = path + episode_name
            # Assign destination with path name and new filename
            # based on files extension
            desmp4 = path + new_episode_list[episode] + '.mp4'
            desmkv = path + new_episode_list[episode] + '.mkv'
            desavi = path + new_episode_list[episode] + '.avi'

            # Rename files based on its extension
            if episode_name[-3:] == 'mp4':
                try:
                    os.rename(src, desmp4)
                except FileNotFoundError:
                    raise SystemExit('Invalid path')
                else:
                    episode += 1

            if episode_name[-3:] == 'mkv':
                try:
                    os.rename(src, desmkv)
                except FileNotFoundError:
                    raise SystemExit('Invalid path')
                else:
                    episode += 1

            if episode_name[-3:] == 'avi':
                try:
                    os.rename(src, desavi)
                except FileNotFoundError:
                    raise SystemExit('Invalid path')
                else:
                    episode += 1
