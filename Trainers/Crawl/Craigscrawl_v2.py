#Craigslist Search
"""
Created on Thu Mar 27 11:56:54 2014
used http://cal.freeshell.org/2010/05/python-craigslist-search-script-version-2/ as
starting point.
"""

import re
import os
import os.path
import time
import urllib2
import webbrowser
from math import *
#import pdb
#pdb.set_trace()

results = re.compile('<p.+</p>', re.DOTALL) #Find pattern for search results.
prices = re.compile('<span class="price".*?</span>', re.DOTALL) #Find pattern for
pages = re.compile('button pagenum">.*?</span>')
delay = 10


def search_all():
    for city in list(set(searchcities)):#add another for loop for all pages

        #Setup headers to spoof Mozilla
        dat = None
        ua = "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.4) Gecko/20091007 Firefox/3.5.4"
        head = {'User-agent': ua}
        errorcount=0

        #Do a quick search to see how many pages of results
        url = "http://" + city + ".craigslist.org/search/" + "sss?s=" + "0" + "&catAbb=sss&query=" + query.replace(' ', '+') + "&minAsk=" + pricemin + "&maxAsk=" + pricemax
        req = urllib2.Request(url, dat, head)
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError:
            if errorcount < 1:
                errorcount = 1
                print "Request failed, retrying in " + str(delay) + " seconds"
                time.sleep(int(delay))
                response = urllib2.urlopen(req)

        msg = response.read()
        errorcount = 0
        pglist = pages.findall(msg)
        pg = pglist.pop(0)
        if pg.find('of') == -1:
            pg=100
        else:
            pg =pg[int((pg.find('of'))+3) : int((pg.find('</span>'))) ]

        if int(pg)/100 == 0:
            pg = 100
        numpages = range(int(pg)/100)


        for page in numpages:
            print "searching...."
            page = page*100
            url = "http://" + city + ".craigslist.org/search/" + "sss?s=" + str(page) + "&catAbb=sss&query=" + query.replace(' ', '+')  + "&minAsk=" + pricemin + "&maxAsk=" + pricemax
            cityurl = "http://" + city + ".craigslist.org"

            errorcount = 0

            #Get page
            req = urllib2.Request(url, dat, head)
            try:
                response = urllib2.urlopen(req)
            except urllib2.HTTPError:
                if errorcount < 1:
                    errorcount = 1
                    print "Request failed, retrying in " + str(delay) + " seconds"
                    time.sleep(int(delay))
                    response = urllib2.urlopen(req)

            msg = response.read()
            errorcount = 0
            res = results.findall(msg)
            res = str(res)
            res = res.replace('[', '')
            res = res.replace(']', '')
            res = res.replace('<a href="' , '<a href="' + cityurl )
            #res = re.sub(prices,'',res)
            res = "<BLOCKQUOTE>"*6 + res + "</BLOCKQUOTE>"*6

            outp = open("craigresults.html", "a")
            outp.write(city)
            outp.write(str(res))
            outp.close()

#This was found at zip code database project
def calcDist(lat_A, long_A, lat_B, long_B):
  distance = (sin(radians(lat_A)) *
              sin(radians(lat_B)) +
              cos(radians(lat_A)) *
              cos(radians(lat_B)) *
              cos(radians(long_A - long_B)))

  distance = (degrees(acos(distance))) * 69.09

  return distance

cities = """
akroncanton:41.043955,-81.51919
ashtabula:41.871212,-80.79178
athensohio:39.322847,-82.09728
cincinnati:39.104410,-84.50774
cleveland:41.473451,-81.73580
columbus:39.990764,-83.00117
dayton:39.757758,-84.18848
limaohio:40.759451,-84.08458
mansfield:40.759156,-82.51118
sandusky:41.426460,-82.71083
toledo:41.646649,-83.54935
tuscarawas:40.397916,-81.40527
youngstown:41.086279,-80.64563
zanesville:39.9461,-82.0122"""

if os.path.exists("craigresults.html")==True:
    os.remove("craigresults.html")

## PROJECT STARTS HERE ###

homecity = "dayton"
radius = raw_input("Search Distance from Home in Miles: ")
query = raw_input("Search Term: ")
pricemin = raw_input("Min Price: ")
pricemax = raw_input("Max Price: ")


#Creates the list and save it in city
citylist = cities.split()

#Create a empty dictionary
citdict = {}
for city in citylist:
    items=city.split(":")
    citdict[items[0]] = items[1]

homecord = str(citdict.get(homecity)).split(",")
print homecord

homelat = float(homecord[0])
homelong = float(homecord[1])

print homelat
print homelong

time.sleep(5)

#Create a set without any elements
searchcities = []
for key,value in citdict.items():
    distcity=key
    distcord=str(value).split(",")
    distlat = float(distcord[0])
    distlong = float(distcord[1])
    dist = calcDist(homelat,homelong,distlat,distlong)
    if dist < int(radius):
        searchcities.append(key)
print searchcities

search_all()
webbrowser.open_new('craigresults.html')