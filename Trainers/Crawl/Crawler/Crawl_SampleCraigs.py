#from craigslist import CraigslistEvents
import craigslist


cl_e = craigslist.CraigslistEvents(site='newyork', filters={'free': True, 'food': True})


for result in cl_e.get_results(sort_by='newest', limit=5):
    print result

'''
{
    'id': u'4866178242',
    'name': u'Lituation Thursdays @ Le Reve',
    'url': u'http://newyork.craigslist.org/mnh/eve/4866178242.html',
    'datetime': u'1/29',
    'price': None,
    'where': u'Midtown East',
    'has_image': True,
    'has_map': True,
    'geotag': None
}
'''