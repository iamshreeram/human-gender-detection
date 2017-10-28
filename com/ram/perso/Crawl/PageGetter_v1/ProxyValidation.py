import random
import re

import requests

from Crawl.LoadUserAgents_v1 import LoadUserAgents

p=re._compile('ab*')

re.compile('ab*',re.IGNORECASE)

proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {"q" : "London,uk"}

# load user agents and set headers
uas = LoadUserAgents()
ua = random.choice(uas)  # select a random user agent
headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

# make the request
r = requests.get(url, proxies=proxy,
    params=params, headers=headers)