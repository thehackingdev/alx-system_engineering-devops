#!/usr/bin/python3
"""Module for task 1 top 10"""


def top_ten(subreddit):
    """Queries the Reddit API"""
    import requests

def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts for
    a given subreddit
    """
    url = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return
    response = response.json()
    if 'data' in response:
        for posts in response.get('data').get('children'):
            print(posts.get('data').get('title'))

    else:
        print(None)
