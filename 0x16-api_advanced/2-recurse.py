#!/usr/bin/python3
"""This function uses recursion to query the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    if after == "STOP":
        return hot_list
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        if not children:
            return None
        hot_list.extend([post['data']['title'] for post in children])
        after = data['data']['after']
        return recurse(subreddit, hot_list, after)
    else:
        return None
