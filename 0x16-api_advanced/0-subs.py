#!/usr/bin/python3
"""
a function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) \
            Gecko/20080214 Firefox/2.0.0.12",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0
