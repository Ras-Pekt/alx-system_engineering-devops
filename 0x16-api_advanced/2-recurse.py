#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) \
            Gecko/20080214 Firefox/2.0.0.12",
    }

    if after is not None:
        url += f"?after={after}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {})

        if "children" not in data:
            return None

        hot_list.append(item["data"]["title"] for item in data["children"])

        after = data.get("after")

        if after is None:
            return hot_list
        else:
            recurse(subreddit, hot_list, after)
    else:
        return None
