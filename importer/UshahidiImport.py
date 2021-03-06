import urllib
import hashlib
import os
import json
import pprint

class UshahidiImport(object):

    def __init__(self, options={}):
        self.data = {}
        self.options = options;

    def _grab_data(self, url, fileprefix, use_cache=False):
        if u'category_id' in self.options:
            url = '%s&by=catid&id=%s' % (url, self.options[u'category_id'])

        if u'limit' in self.options:
            url = '%s&limit=%s' % (url, self.options[u'limit'])

        url_hash = hashlib.sha224(url).hexdigest()
        file_name = "%s-%s.json" % (fileprefix, url_hash)
        print url

        has_cache = False
        if use_cache:
            if os.path.isfile(file_name):
                use_cache = True

        if ((not use_cache) or (not has_cache)):
            file_handler, header = urllib.urlretrieve(url, file_name)
        
        with open(file_name) as data_file:
            payload = json.load(data_file)
            self.data = payload[u'payload'][u'incidents']

        return self.data

    def transform_row(self, incident_data):
        pprint.pprint(incident_data) 
        incident = incident_data[u'incident']
        custom_fields = incident_data[u'customfields']
        comments = incident_data[u'comments']
        media = incident_data[u'media']  
        categories = incident_data[u'categories']

