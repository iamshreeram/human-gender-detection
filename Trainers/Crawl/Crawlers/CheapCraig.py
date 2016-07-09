#Variable declaration and imports
import re
import os
import os.path
import time
import urllib2
import webbrowser
from math import *

results = re.compile('<p.+</p>', re.DOTALL) #Find pattern for search results.
prices = re.compile('<span class="price".*?</span>', re.DOTALL) #Find pattern for
pages = re.compile('button pagenum">.*?</span>')
delay = 10

###########Product details and scrap cities and create url list
#1.0. prodcut details
#def get_product_details():
homecity = "fayar"
radius = raw_input("Search Distance from Home in Miles: ")
query = raw_input("Search Term: ")
pricemin = raw_input("Min Price: ")
pricemax = raw_input("Max Price: ")


######## In Future Scope ############
#2. create a url SET from cities
#def get_craig_cities():
	#2.1.1. check if there is any records on craigs_cities_set set
	#2.1.2. If Cities available, clean craigs_cities_set set
	#2.1.3. Else, Create a new dictionary
# *********************************** #
# Current Scope #
#take a SET with single url in it
craigs_cities_link = ['http://fayar.craigslist.org/']
craigs_cities_url  = []

#http://fayar.craigslist.org/search/sss?query=canon+6d&sort=rel&min_price=10&max_price=10000
#Creating URL
#"http://" + city + ".craigslist.org/search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
url = "http://fayar.craigslist.org/" + "search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
ua = "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.4) Gecko/20091007 Firefox/3.5.4"
#Chrome User agent : Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
head = {'User-agent': ua}
errorcount = 0
dat = None

req = urllib2.Request(url, dat, head)


#3. crawl url from SET and save
#3.1. Crawl URL
#def get_url_crawlers():
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
#return msg;

#3.2. Save the crawled page to variable curr_city_state




### Out of scope #############
#4. find if there is any <link rel> with next page true
#	4.1 Next page search


#5. if there is any next page, catch that link with regular expression Go to step 3
#5.1 If next page exists, Call 3.2



#6. Capture required details and format
#6.1 Capture Required details -
#def format_details:
city = "fayar"
cityurl = "http://fayar.craigslist.org/"
res = results.findall(msg)
print res
time.sleep(10)

res = str(res)
print res
time.sleep(10)

res = res.replace('[', '')
print res
time.sleep(10)

res = res.replace(']', '')
print res
time.sleep(10)


res = res.replace('<a href="' , '<a href="' + cityurl )
print res
time.sleep(10)


#res = re.sub(prices,'',res)
res = "<BLOCKQUOTE>"*3 + res + "</BLOCKQUOTE>"*3
print res
time.sleep(10)


outp = open("craigresults.html", "a")


outp.write(city)

outp.write(str(res))
print str(res)
time.sleep(10)

outp.close()

#7. Print report details
#def publish_report():
webbrowser.open_new('craigresults.html')