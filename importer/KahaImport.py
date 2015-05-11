import json
import urllib
from dateutil import parser
from kaha import models
import os

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

    def __init__(self, options={}):
        self.data = {}
        self.options = options

    def grab_data(self, use_cache=False):
        has_cache = False
        file_name = 'kaha-data.json'
        if use_cache:
            if os.path.isfile(file_name):
                has_cache = True

        if ((not use_cache) or (not has_cache)):
            kaha_url = 'http://kaha.co/api'
            file_handler, header = urllib.urlretrieve(kaha_url, file_name)

        with open(file_name) as data_file:
            self.data = json.load(data_file)
        return self.data

    def fixDitrict(self, district):
        corrected = district
        if district == u'Sindhupalchok':
            corrected = 'Sindhupalchowk'
        elif district == u'Kavrepalanchok':
            corrected = 'Kavre'
        return corrected

    def transform_row(self, row):
        resource = models.KahaResource()
        resource.data_source.append(models.KahaResourceSource(source='kaha', source_id=row[u'uuid'], source_json=json.dumps(row)))
        resource.district = self.fixDitrict(row[u'location'][u'district'].title())
        resource.tole = row[u'location'][u'tole'].title()
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
                s = models.KahaResourceProperty(key='stat_%s' % _key, value=_value)
                resource.props.append(s)

        return resource

    def find_record(self, row, db):
        return db.session.query(models.KahaResourceSource).filter_by(source_id=row[u'uuid'], source='kaha').first()
