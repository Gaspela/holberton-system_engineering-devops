#!/usr/bin/python3
""" Reddit API """
import requests


def number_of_subscribers(subreddit):
    try:
        r = requests.get('https://www.reddit.com/r/{}/about.json'.
                         format(subreddit),
                         headers={'User-Agent': 'custom'},
                         allow_redirects=False)
        return r.json().get('data').get('subscribers')
    except:
        return 0
