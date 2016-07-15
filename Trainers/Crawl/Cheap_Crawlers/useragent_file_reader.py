import re
import os
import os.path
import time
import urllib2
import webbrowser
from math import *

ua_expr = re.compile(r'\"(.*?)\"')

#<a href="// >
#file = open('UserAgent','r')
#print file.read()

print "\n*****************\n"

ua_file = open('UserAgent','r')
useragent = ua_file.read()
ua_agents = ua_expr.findall(useragent)
print ua_agents

time.sleep(10)

'''
values = [w.replace('<a href="//', '') for w in values]
#print values

values = [w.replace('">', '') for w in values]
print values

radius = raw_input("Search Distance from Home in Miles: ")
query = raw_input("Search Term: ")
pricemin = raw_input("Min Price: ")
pricemax = raw_input("Max Price: ")

for i in values:
    #curr_url = values.pop(i)
    url = "http://"+ i + "search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
    print url
'''