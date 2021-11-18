# Code at: https://gist.github.com/AO8/74a3a81fd672a6f8d0cc149ed62295de

import requests

def get_joke():
  """fetches and prints a random joke"""
  url = "http://api.icndb.com/jokes/random"
  resp = requests.get(url)
  resp.encoding = "utf-8"
  data = resp.json()
  print(data["value"]["joke"])

get_joke()
