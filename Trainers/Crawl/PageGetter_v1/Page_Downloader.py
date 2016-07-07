import HTMLParser
import urllib
import time

#Pulls all strings from the website

urlText = []

#Define HTML Parser
class parseText(HTMLParser.HTMLParser):

    def handle_data(self, data):
        #if data != '\n':
        urlText.append(data)
        print urlText
        time.sleep(2)


#Create instance of HTML parser
lParser = parseText()

thisurl = "http://www-rohan.sdsu.edu/~gawron/index.html"
#Feed HTML file into parser
lParser.feed(urllib.urlopen(thisurl).read())
lParser.close()
for item in urlText:
    print item