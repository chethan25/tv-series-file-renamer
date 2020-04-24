# -*- coding: utf-8 -*-
"""
Module to rename the files
"""
import os
import sys

import scraper
from main import path
from filenames_sort import sorted_alphanumeric


new_season_dict = scraper.season_dict

for season_no, episode_list in new_season_dict.items():
    # Modifying path name to include season directory
    # based on operating system platform
    if sys.platform.startswith('linux'):
        new_path = path + 'S' + str(season_no) + '/'
    elif sys.platform == 'win32':
        new_path = path + 'S' + str(season_no) + '\\'
    elif sys.platform == 'darwin':
        new_path = path + 'S' + str(season_no) + '/'
    else:
        raise SystemExit('Unsupported operating system')

    episode = 0

    for episode_name in sorted_alphanumeric(os.listdir(new_path)):
        # Assign src with files path name
        src = new_path + episode_name
        # Assign destination with path name and new filename
        # based on files extension
        desmp4 = new_path + episode_list[episode] + '.mp4'
        desmkv = new_path + episode_list[episode] + '.mkv'
        desavi = new_path + episode_list[episode] + '.avi'

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
