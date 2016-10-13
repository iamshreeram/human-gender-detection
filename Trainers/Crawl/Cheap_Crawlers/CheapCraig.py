# Variable declaration and imports
import random
import time
import traceback
import urllib2
import webbrowser

import os
import os.path
import os.path
import re

results = re.compile('<p.+</p>', re.DOTALL)  # Find pattern for search results.
prices = re.compile('<span class="price".*?</span>', re.DOTALL)  # Find pattern for
pages = re.compile('button pagenum">.*?</span>')
new_line = re.compile('\n.*?\n')
delay = 10

# To find the list of urls
def get_urllist():
    url_file = 'urllist'
    with open(url_file) as fpointer:
        lines = fpointer.read().splitlines()
    return lines


# url_file = url + "search/" + "sss?query=" + query.replace(' ','+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
# time.sleep(100)
# url_file = url + "search/" + "sss?query=" + query.replace(' ',
# To get any 1 browser agent
# <editor-fold desc="User agent">
# </editor-fold>
# To check if the file exist already. If so, Remove it


def get_agent():
    agent = random.choice(agentreader)
    return agent

def reportfile_exists():
    filename = 'craigresults.html'
    if os.path.isfile(filename):
        try:
            os.remove(filename)
            print "file exists"
        except OSError:
            pass
            traceback.print_exc()
    else:
        print "file doesnt exist"



###########Product details and scrap cities and create url list
# 1.0. prodcut details
# def get_product_details():
# radius = raw_input("Search Distance from Home in Miles: ")



######## In Future Scope ############
# 2. create a url SET from cities
# def get_craig_cities():
# 2.1.1. check if there is any records on craigs_cities_set set
# 2.1.2. If Cities available, clean craigs_cities_set set
# 2.1.3. Else, Create a new dictionary
# *********************************** #
# Current Scope #
# take a SET with single url in it
# craigs_cities_link = ['http://fayar.craigslist.org/']
# craigs_cities_url = []
# http://fayar.craigslist.org/search/sss?query=canon+6d&sort=rel&min_price=10&max_price=10000
# Creating URL
# "http://" + city + ".craigslist.org/search/" + "sss?query=" + query.replace(' ', '+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
# url = "http://fayar.craigslist.org/" + "search/" + "sss?query=" + query.replace(' ','+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
# ua = "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.4) Gecko/20091007 Firefox/3.5.4"
# Chrome User agent : Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36



# 3. crawl url from SET and save
# 3.1. Crawl URL
# def get_url_crawlers():
# Request sent to server here

def parse_url(curr_url, dat, UserAgent):
    homecity = "fayar"
    '''
    query = raw_input("Search Term: ")
    pricemin = raw_input("Min Price: ")
    pricemax = raw_input("Max Price: ")
    '''
    req = urllib2.Request(curr_url, dat, UserAgent)
    print "Im going to hit this url:",curr_url
    #time.sleep(1)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError:
        if errorcount < 1:
            errorcount = 1
            print "Request failed, retrying in " + str(delay) + " seconds"
            time.sleep(int(delay))
            response = urllib2.urlopen(req)
    except urllib2.URLError:
        print "Error in URL. Moving on to next state."

    msg = response.read()
    res = results.findall(msg)
    return res

# print "\n\n\n\n******************\n\n"
# print res
## Out of scope #############
# 4. find if there is any <link rel> with next page true
#	4.1 Next page search
# 5. if there is any next page, catch that link with regular expression Go to step 3
# 5.1 If next page exists, Call 3.2
# 6. Capture required details and format
# 6.1 Capture Required details -
# def format_details:
#time.sleep(10)
# time.sleep(10)
# res = re.sub(prices,'',res)
# time.sleep(10)
# time.sleep(10)
# 7. Print report details
# def publish_report():
# itemlist_creation() --> is called inside below function

#Adding a new line make new commit
def itemlist_creation(cityurl,res):
    print "res value inside itemlist_creation function :",res
    #time.sleep(1)
    # city = "Fayetville"
    # cityurl = "http://fayar.craigslist.org"
    items_curr_city = re.sub(r'\n.*\n', '', res[0], flags=re.IGNORECASE)
    # print "New message : ", items_curr_city
    res = items_curr_city
    print "Value of current city: ", res
    # time.sleep(10)
    res = str(res)
    if "<a href=\"/msg/" in res:
        res = res.replace('<a href="', '<a href="' + cityurl)
    else:
        print "URLs are already added with city url"
    # print "HREF of result:", res
    #time.sleep(2)
    # print res
    res = "<BLOCKQUOTE>" * 3 + res + "</BLOCKQUOTE>" * 3
    #print res
    outp = open("craigresults.html", "a")
    # time.sleep(2)
    # outp.write(city)
    outp.write(str(res))
    #print "Done with writing to file"
    # print str(res)
    outp.close()
    return True

# print "res value inside is_empty function :",res
# time.sleep(4)
def is_notempty(any_structure):
    if any_structure:
        return True
    else:
        return False

def reslist_creator(url,res):
    if is_notempty(res):
        print('Few of your search items found. Analysing the details further..')
        itemlist_creation(url,res)
    else:
        print('Items not found. Moving to next state.')

# return msg;
# print msg
# time.sleep(100)
# 3.2. Save the crawled page to variable curr_city_state

if __name__ == "__main__":
    print "running craigslist"
    time.sleep(1)
    query = "Manfrotto MT055CXPRO4"
    pricemin = "50"
    pricemax = "400"
    agentfile = 'UserAgent'
    agentreader = open(agentfile).read().splitlines()
    reportfile_exists()

    lines = get_urllist()
    for url in lines:
        curr_url = url + "/search/" + "sss?query=" + query.replace(' ','+') + "&sort=rel&minAsk=" + pricemin + "&maxAsk=" + pricemax
        user_agent = get_agent()
        UserAgent = {'User-agent': user_agent}
        errorcount = 0

        dat = None
        # print curr_url
        res = parse_url(curr_url, dat, UserAgent)
        # print "CURRENT URL : ", curr_url
        reslist_creator(curr_url,res)
        #time.sleep(2)

    webbrowser.open_new('craigresults.html')