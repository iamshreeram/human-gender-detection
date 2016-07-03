from lxml.html import parse
from urllib2 import urlopen
from pandas.io.parsers import TextParser

def _unpack (row,kind='td'):
    elts = row.findall('.//%s' % kind)
    return [val.text for val in elts]

def parse_options_data (table):
    rows = table.findall('.//tr')
    header = _unpack(rows[0],kind='th')
    data = [_unpack(r) for r in rows[1:]]
    return TextParser(data,names=header).get_chunk()

if __name__ == '__main__':
    #parsed = parse('http://finance.yahoo.com/q/op?s=AAPL+Options')
    #parsed = parse('http://www-rohan.sdsu.edu/~gawron')
    #parsed = parse('http://www.lajollasurf.org/cgi-bin/plottide.pl')

    url = 'http://www.ezfshn.com/tides/usa/california/san%20diego'
    parsed = parse(url)

    #id="ctl00_ctl00_Content_MCC_RadDatePicker_calendar_Top"

    doc = parsed.getroot()
    links = doc.findall('.//a')
    links_sub_list = links[15:20]
    lnk = links_sub_list[0]
    sample_url = lnk.get('href')
    sample_display_text = lnk.text_content()
    tables = doc.findall('.//table')
    ## Look at tables,  find a table of interest
    #puts = tables[9]
    ## Ditto
    #calls = tables[13]
    dt = tables[0]
    rows = dt.findall('.//tr')
    headers = _unpack(rows[0],kind='th')
    row_vals =  _unpack(rows[1],kind='td')

    #call_data = parse_options_data(calls)
    tide_data = parse_options_data(dt)
    print tide_data[:10]