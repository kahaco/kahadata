import json
from pprint import pprint
from app import db, models
from dateutil import parser
import sys

with open('data.json') as data_file:
    data = json.load(data_file)


#pprint(data)
"""
{u'active': u'true',
 u'description': {u'contactname': u'--',
                  u'contactnumber': u'--',
                  u'detail': u'Binayak Basti Balaju Alongside Bishnumati River',
                  u'title': u'Binayak Basti Balaju'},
 u'location': {u'district': u'kathmandu', u'tole': u'thakali samaj ghar'},
 u'stat': {u'helpedctr': u'0', u'unavlblctr': u'0', u'wrngdtactr': u'0'},
 u'type': u'shelter',
 u'uuid': u'5b7cfcdd00e420f892e3e252a1e41d24dc57c58a'
}
"""
for d in data:

    pprint(d)
    try:
        r = models.KahaResource()
        r.uuid = d[u'uuid']
        r.district = d[u'location'][u'district']
        r.tole = d[u'location'][u'tole']
        r.title = d[u'description'][u'title']
        r.description = d[u'description'][u'detail']
        r.contactname = d[u'description'][u'contactname']
        r.contactnumber = d[u'description'][u'contactnumber']
        if 'date' in d:
            r.updated = parser.parse(d[u'date'][u'modified'])
            if d[u'date'][u'created']:
                r.craeted = parser.parse(d[u'date'][u'created'])

        r.types.append(models.KahaResourceType(resource_type=d[u'type']))
        if 'stat' in d:
            for _key, _value in d[u'stat'].iteritems():
                s = models.KahaResourceStat(key=_key,value=_value)
                r.stats.append(s)

        db.session.add(r)
        db.session.commit()
    except:
        db.session.rollback()
        print "Unexpected error:", sys.exc_info()[0]

