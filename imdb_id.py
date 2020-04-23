# -*- coding: utf-8 -*-
"""
Module to get imdb id of the tv series using omdbapi
"""
import json
import requests

from main import tv_series_name


# Omdbapi website url
url = f'https://www.omdbapi.com/?t={tv_series_name}&apikey=f64b87dd'
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
    # Getting json object
    tv_series_json = req.json()
    # Finding imdb id based on the key 'imdbID'
    imdb_id = tv_series_json['imdbID']
