from lxml.html import parse
from urllib2 import urlopen
from pandas.io.parsers import TextParser
from time import sleep as slp

def _unpack (row,kind='td'):
    print "Enters the unpack"
    elts = row.findall('.//%s' % kind)
    print "Elts ", elts
    slp(2)
    return [val.text for val in elts]

def parse_options_data (table):
    print "Enters the Parse option"
    rows = table.findall('.//tr')
    header = _unpack(rows[0],kind='th')
    data = [_unpack(r) for r in rows[1:]]
    print "Data : ", data
    slp(2)
    return TextParser(data,names=header).get_chunk()

if __name__ == '__main__':
    print "Enters __main__ function"
    #parsed = parse('http://finance.yahoo.com/q/op?s=AAPL+Options')
    #parsed = parse('http://www-rohan.sdsu.edu/~gawron')
    #parsed = parse('http://www.lajollasurf.org/cgi-bin/plottide.pl')

    url = 'http://www.ezfshn.com/tides/usa/california/san%20diego'
    parsed = parse(url)
    #name = parsed

    #id="ctl00_ctl00_Content_MCC_RadDatePicker_calendar_Top"

    slp(10)
    doc = parsed.getroot()
    print "Doc : ",doc
    slp(2)

    links = doc.findall('.//a')
    print "Links : ",links
    slp(2)

    links_sub_list = links[15:20]
    print "Links sub list : ", links_sub_list
    slp(2)

    lnk = links_sub_list[0]
    print "Lnk : ", lnk
    slp(2)

    sample_url = lnk.get('href')
    print "Sample url", sample_url
    slp(2)

    sample_display_text = lnk.text_content()
    print "Sample display text", sample_display_text
    slp(2)

    tables = doc.findall('.//table')
    print "Tables: ", tables
    ## Look at tables,  find a table of interest
    #puts = tables[9]
    ## Ditto
    #calls = tables[13]
    slp(2)

    dt = tables[0]
    rows = dt.findall('.//tr')
    headers = _unpack(rows[0],kind='th')
    row_vals =  _unpack(rows[1],kind='td')
    slp(2)
    #call_data = parse_options_data(calls)
    tide_data = parse_options_data(dt)
    print tide_data[:10]