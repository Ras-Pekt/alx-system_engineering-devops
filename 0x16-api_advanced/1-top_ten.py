#!/usr/bin/python3
"""
a function that queries the Reddit API
and prints the titles of the first 10 hot posts listed
for a given subreddit
"""

import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) \
            Gecko/20080214 Firefox/2.0.0.12",
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        hot_list = []
        for key in response.json().get("data").get("children"):
            print(f"{key.get('data').get('title')}")
            hot_list.append(key.get('data').get('title'))
        if len(hot_list) == 0:
            print("None")
    else:
        print("None")
