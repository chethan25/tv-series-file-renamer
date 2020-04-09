# -*- coding: utf-8 -*-
"""
Module to get and parse the tv series episodes name from imdb website
"""
import sys

import requests

from bs4 import BeautifulSoup

# Tv series imdb website url
url = 'https://www.imdb.com/title/tt0096697/episodes?season=4'
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
    raise SystemExit('A Connection error occurred')
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
