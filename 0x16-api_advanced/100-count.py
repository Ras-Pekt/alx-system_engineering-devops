#!/usr/bin/python3
"""
a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.8.1.12) \
            Gecko/20080214 Firefox/2.0.0.12",
    }

    params = {'after': after}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    data = response.json().get('data', {})

    posts = data.get('children', None)
    if posts is None:
        return None

    for post in posts:
        word_list.append(post.get('data', {}).get('title'))

    after = data.get('after')
    if after is None:
        return word_list
    return count_words(subreddit, word_list, after)
