import re
import os
import os.path
import time
import urllib2
import webbrowser
from math import *

hreftag_remover = re.compile('<a href=\"//.*?>')
dotorg_chooser = re.compile('.*?org.*?')


#<a href="// >
#file = open('UserAgent','r')
#print file.read()

print "\n*****************\n"

craigsfile = open('craigs_html','r')
msg = craigsfile.read()

values = hreftag_remover.findall(msg)
print values


#print values.pop()

#finds the US locations

#Searchs only Org value
lambdavalue = filter(lambda x:re.search(r'.org', x), values)
lambdavalue = filter(lambda x:re.search('^(?!.*www\.craigslist).*$', x), lambdavalue)
print "Lambda value : ", lambdavalue
time.sleep(100)

#values = dotorg_chooser.findall(values)
#print values


time.sleep(100)

#this will remove all href HTML tags
values = [w.replace('<a href="//', '') for w in values]
values = [w.replace('">', '') for w in values]
print values


#To remove all files other than US
#values

radius = raw_input("Search Distance from Home in Miles: ")
query = raw_input("Search Term: ")
pricemin = raw_input("Min Price: ")
pricemax = raw_input("Max Price: ")

for i in values:
    #curr_url = values.pop(i)
    url = "http://"+ i + "search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
    print url
