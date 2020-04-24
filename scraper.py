# -*- coding: utf-8 -*-
"""
Module to get and parse the tv series episodes name from imdb website
"""
import os
import sys
import time
import requests

from bs4 import BeautifulSoup

from main import path
from imdb_id import imdb_id


# Finding no of seasons present in the directory
no_of_seasons = len(os.listdir(path))

season_dict = {}

for season in range(1, no_of_seasons + 1):
    # Tv series imdb website url
    url = f'https://www.imdb.com/title/{imdb_id}/episodes?season={season}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0)\
        Gecko/20100101 Firefox/74.0'
        }

    try:
        req = requests.get(url, headers=headers, timeout=2)
        req.raise_for_status()
    except requests.exceptions.HTTPError:
        raise SystemExit('An HTTP error occurred')
    except requests.exceptions.ConnectionError:
        raise SystemExit('A connection error occurred')
    except requests.exceptions.Timeout:
        raise SystemExit('The request timed out')
    except requests.exceptions.RequestException:
        raise SystemExit('There was an ambiguous exception that occurred\
            while handling your request')
    else:
        soup = BeautifulSoup(req.text, 'lxml')

        episode_no_odd, episode_no_even = 1, 2

        episode_dict = {}
        episode_list = []

        for tag in soup.find_all('div', class_='list_item odd'):
            tag1 = tag.find('div', class_='info')
            episode_name_odd = tag1.a.text
            episode_dict[episode_no_odd] = episode_name_odd
            episode_no_odd += 2

        for tag in soup.find_all('div', class_='list_item even'):
            tag1 = tag.find('div', class_='info')
            episode_name_even = tag1.a.text
            episode_dict[episode_no_even] = episode_name_even
            episode_no_even += 2

        for episode in sorted(episode_dict.keys()):
            episode_list.append(f'{episode} - {episode_dict[episode]}')

        # Inserting each seasons episode names list to a dictionary
        season_dict[season] = episode_list
        print(f'Season {season} extracted')
        # Suspending execution for the amount of time to get the response
        time.sleep(req.elapsed.total_seconds())
