#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0 """
import requests
import json


def recurse(subreddit, hot_list=[]):
  """Gets a list of the hot articles for a given subreddit.

  Args:
    subreddit: The name of the subreddit.
    hot_list: A list of the titles of the hot articles that have already been
      retrieved.

  Returns:
    A list of the titles of all hot articles for the given subreddit.
  """

  url = "https://api.reddit.com/r/{}/hot?limit=25".format(subreddit)
  agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0)'
  agent += ' Gecko/20100101 Firefox/102.0'
  headers = {"user-Agent": agent}
  response = requests.get(url, headers=headers, allow_redirects=False)
  if response.status_code == 200:
    data = json.loads(response.content)
    articles = data["data"]["children"]
    for article in articles:
      hot_list.append(article["data"]["title"])
    if data["data"].get("after"):
      return recurse(subreddit, hot_list)
    else:
      return hot_list
  else:
    return None
