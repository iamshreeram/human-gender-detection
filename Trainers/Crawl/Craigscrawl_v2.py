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
    for city in list(set(searchcities)):
        #add another for loop for all pages

        #Setup headers to spoof Mozilla
        dat = None
        ua = "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.4) Gecko/20091007 Firefox/3.5.4"
        #Chrome User agent : Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
        head = {'User-agent': ua}
        errorcount=0

        #Do a quick search to see how many pages of results
        #url = "http://" + city + ".craigslist.org/search/" + "sss?s=" + "0" + "&catAbb=sss&query=" + query.replace(' ', '+') + "&minAsk=" + pricemin + "&maxAsk=" + pricemax
        #print "Program URL : ", url
        #http://columbus.craigslist.org/search/sss?query=canon&sort=rel&min_price=10&max_price=2000  ------------- Original URL
        #http://columbus.craigslist.org/search/sss?s=0&catAbb=sss&query=canon&minAsk=10&maxAsk=20000 ------------- From Python Code

        """ CHANGED URL FORMAT FROM ORIGINAL SCRIPT """
        url = "http://" + city + ".craigslist.org/search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
        #print "Latest URL : ", url

        #http://columbus.craigslist.org/search/sss?query=canon&sort=rel&min_price=10&max_price=2000
        #http://columbus.craigslist.org/search/sss?query=canon+6d&sort=rel&min_price=10&max_price=2000

        request_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }

        time.sleep(2)
        print "URL is : ", url
        #Request creation happens here
        req = urllib2.Request(url, dat, head)
        #req = urllib2.Request(url, headers=request_headers)
        #req.add_header('Accept-Language','en-US,en;q=0.8')
        #req.add_header('Accept-Encoding','gzip, deflate, sdch')
        time.sleep(5)

        '''
        request_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        "Accept-Encoding": "gzip, deflate, sdch"
        "Accept-Language": "en-US,en;q=0.8"
        "Connection":"keep-alive"
        "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        }
        '''

        try:
            #Request sent to server here
            response = urllib2.urlopen(req)
        except urllib2.HTTPError:
            if errorcount < 1:
                errorcount = 1
                print "Request failed, retrying in " + str(delay) + " seconds"
                time.sleep(int(delay))
                response = urllib2.urlopen(req)

        msg = response.read()
        print "\n ************** PAGE IS ***************** \n", msg
        print "\n **************************************** \n"
        time.sleep(3)

        errorcount = 0
        pglist = pages.findall(msg)
        print "\n \n PAGE LIST IS \n \n", pglist
        print "\n\n\n ******************** \n\n\n"
        time.sleep(3)


        pg = pglist.pop(0)
        print "*********** PG ************ ", pg
        time.sleep(3)


        ##############  LOGIC TO CRAWL EACH PAGE IN WEBSITE ################

        if pg.find('of') == -1:
            pg=100
            print pg

        else:
            pg =pg[int((pg.find('of'))+3) : int((pg.find('</span>'))) ]
            print pg

        if int(pg)/100 == 0:
            pg = 100
        numpages = range(int(pg)/100)
        print "NUMBER OF PAGES : ", numpages
        time.sleep(3)

        for page in numpages:
            print "searching..."
            page = page*100

            url = "http://" + city + ".craigslist.org/search/" + "sss?s=" + str(page) + "&catAbb=sss&query=" + query.replace(' ', '+')  + "&minAsk=" + pricemin + "&maxAsk=" + pricemax

            '''
            ######### If condition is to choose the url for searching ..
            ######################################
            if page.pop(0) > 0:
                url = "http://" + city + ".craigslist.org/search/" + "sss?s=" + str(page) + "&query=" + query.replace(' ', '+')  + "&minAsk=" + pricemin + "&maxAsk=" + pricemax
                #&catAbb=sss
            else :
                url = "http://" + city + ".craigslist.org/search/" + "sss?s=" + str(page) + "&query=" + query.replace(' ', '+')  + "&minAsk=" + pricemin + "&maxAsk=" + pricemax
            '''
            cityurl = "http://" + city + ".craigslist.org"

            errorcount = 0
            print url
            time.sleep(100)

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
  print "Distance is : ", distance

  return distance


#These are the city list that our crawler will crawl and loook for items
#Latitute and Longitutes are to check if the city is with in radius
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


#Creates the list and saves city
#Remove below comments -- This is to skip to direct values
'''
citylist = cities.split()

#Create a empty dictionary
citdict = {}
for city in citylist:
    #Split and create the city list in items
    items=city.split(":")
    #Create the dictionary with items
    citdict[items[0]] = items[1]

#Home coordinates
homecord = str(citdict.get(homecity)).split(",")
#print "Home Cord : ", homecord


homelat = float(homecord[0])
homelong = float(homecord[1])

'''

#print "Latitude : ", homelat
#print "Longit : ", homelong

#time.sleep(3)

#print "Citdict items :", citdict.items()

#Create a LIST without any elements to add the cities
#Remove the comments below -- This is to skip forloop of searching cities
'''
searchcities = []
for key,value in citdict.items():
    #Choose single city to find if the radius is less within range
    distcity=key

    #Choose the co-ordinate of the city and puts in variable distcord
    distcord=str(value).split(",")
    distlat = float(distcord[0])
    distlong = float(distcord[1])

    #Calculate the distance between the current location
    #This is to see if the item is within radius
    dist = calcDist(homelat,homelong,distlat,distlong)
    if dist < int(radius):
        #Adds the cities that are with in the radius range to LIST
        searchcities.append(key)

#print "Overall LIST value :", searchcities
'''
searchcities =['columbus']

search_all()
webbrowser.open_new('craigresults.html')