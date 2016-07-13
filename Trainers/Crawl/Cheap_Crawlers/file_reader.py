import re
import os
import os.path
import time
import urllib2
import webbrowser
from math import *

new_line = re.compile('<a href=\"//.*?>')

#<a href="// >
#file = open('UserAgent','r')
#print file.read()

print "\n*****************\n"

file1 = open('craigs_html','r')
msg = file1.read()
values = new_line.findall(msg)
print values

'''
values = values.replace('<a href="//' , ' ' )
print values
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




























