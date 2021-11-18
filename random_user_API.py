# Code at: https://gist.github.com/AO8/74a3a81fd672a6f8d0cc149ed62295de

import requests

def get_random_user():
  """Print a random user"""
  url = "https://randomuser.me/api"
  resp = requests.get(url)
  resp.encoding = "utf-8"
  data = resp.json()        # Dictionary
  # Get first name, last name and email
  print(data["results"][0].get("name").get("first") + "\n" + data["results"][0].get("name").get("last") + "\n" + data["results"][0].get("email"))


get_random_user()
