#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0 """
import requests
import sys


def top_ten(subreddit):
    """the function"""
    """url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url)

    dico = response.json()"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)'
    agent += ' Gecko/20100101 Firefox/102.0'
    headers = {"user-Agent": agent}
    response = requests.get(url, headers=headers, allow_redirects=False)
    return 0 if response.status_code != 200 else response.json()\
        .get('data')\
        .get('subscribers')
