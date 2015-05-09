import urllib
import os
import json
import pprint

class UshahidiImport(object):

    def __init__(self):
        self.data = {}

    def _grab_data(self, data_url, file_name, use_cache=False):
        has_cache = False
        if use_cache:
            if os.path.isfile(file_name):
                use_cache = True

        if ((not use_cache) or (not has_cache)):
            file_handler, header = urllib.urlretrieve(data_url, file_name)
        
        with open(file_name) as data_file:
            payload = json.load(data_file)
            self.data = payload[u'payload'][u'incidents']

        return self.data

    def transform_row(self, incident):
        pprint.pprint(incident) 
