import json
import urllib
from dateutil import parser
from kaha import models

class KahaImport:
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

    def __init__(self):
        self.data = {}

    def grab_data(self):
        kaha_url = 'http://kaha.co/api'
        file_handler, header = urllib.urlretrieve(kaha_url, 'kaha-data.json')
        with open(file_handler) as data_file:
            self.data = json.load(data_file)
        return self.data

    def transform_row(self, row):
        resource = models.KahaResource()
        resource.datasource = u'kaha'
        resource.uuid = row[u'uuid']
        resource.district = row[u'location'][u'district'].lower()
        resource.tole = row[u'location'][u'tole'].lower()
        resource.title = row[u'description'][u'title']
        resource.description = row[u'description'][u'detail']
        if 'contactname' in row[u'description']:
            resource.contactname = row[u'description'][u'contactname']
        if 'contactname' in row[u'description']:
            resource.contactnumber = row[u'description'][u'contactnumber']

        resource_for = u'supply'
        if 'channel' in row:
            resource_for = row[u'channel']
        resource.resource_for = resource_for

        if 'date' in row:
            resource.updated = parser.parse(row[u'date'][u'modified'])
            if row[u'date'][u'created']:
                resource.craeted = parser.parse(row[u'date'][u'created'])

        resource.types.append(models.KahaResourceType(resource_type=row[u'type']))
        if 'stat' in row:
            for _key, _value in row[u'stat'].iteritems():
                s = models.KahaResourceStat(key=_key,value=_value)
                resource.stats.append(s)

        return resource

    def find_record(self, row, db):
        return db.session.query(models.KahaResource).filter_by(uuid=row.uuid).first()
