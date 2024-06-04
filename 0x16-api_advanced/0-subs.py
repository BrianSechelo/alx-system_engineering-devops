#!/usr/bin/python3
"""This function queries the Redit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """Retuns the total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
