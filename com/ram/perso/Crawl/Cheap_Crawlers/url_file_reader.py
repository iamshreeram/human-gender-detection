import re
import os
import os.path
from time import sleep as s
import urllib2
import webbrowser
from math import *
import urllib
from bs4 import BeautifulSoup as bs
from lxml import etree as e


hreftag_remover = re.compile('<a href=\"//.*?>')
dotorg_chooser = re.compile('.*?org.*?')

print "\n*****************\n"
craigsfile = open('craigs_html','r')
msg = craigsfile.read()

#s(100)

values = hreftag_remover.findall(msg)
print values

#s(100)

#values = dotorg_chooser.findall(values)
#print values

#s(100)

#this will remove all href HTML tags
values = [w.replace('<a href="//', '') for w in values]
values = [w.replace('">', '') for w in values]
print values


#print values.pop()
#finds the US locations
#Searchs only Org value
lambdavalue = filter(lambda x:re.search(r'.org', x), values)
lambdavalue = filter(lambda x:re.search('^(?!.*www\.craigslist).*$', x), lambdavalue)
print "Lambda value : ", lambdavalue

#To remove all files other than US
#values
'''
radius = raw_input("Search Distance from Home in Miles: ")
query = raw_input("Search Term: ")
pricemin = raw_input("Min Price: ")
pricemax = raw_input("Max Price: ")
'''
outp = open("urllist_list", "ab+")

for i in lambdavalue:
    #curr_url = values.pop(i)
    #url = "http://"+ i + "search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
    url = "http://"+ i +"\n"
    print url
    outp.write(url)