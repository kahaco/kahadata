import UshahidiImport
import hashlib

class SparrowImport(UshahidiImport.UshahidiImport):
    """
    {u'categories': [{u'category': {u'id': 1, u'title': u'Help Needed'}}],
     u'comments': [],
     u'customfields': [],
     u'incident': {u'incidentactive': u'1',
                   u'incidentdate': u'2015-05-08 06:44:00',
                   u'incidentdescription': u'Help bhadrawas-4,Kathmandu. help for earthquake victims\n\nContact: 9841305399',
                   u'incidentid': u'1380',
                   u'incidentmode': u'2',
                   u'incidenttitle': u'Help needed at Bhadrawas - 4 Kathmandu.',
                   u'incidentverified': u'0',
                   u'locationid': u'2098',
                   u'locationlatitude': u'27.707676',
                   u'locationlongitude': u'85.314888',
                   u'locationname': u'Kathmandu, Bagmati, Central Development Region, Nepal'},
     u'media': []}
    """

    def grab_data(self, use_cache=False):
        url = 'http://help.sparrowsms.com/api?task=incidents'
        if u'category_id' in self.options:
            url = '%s&by=catid&id=%s' % (url, self.options[u'category_id'])

        if u'limit' in self.options:
            url = '%s&limit=%s' % (url, self.options[u'limit'])

        url_hash = hashlib.sha224(url).hexdigest()
        print url
        return self._grab_data(url, 'sparrowsms-data-%s.json' % (url_hash), use_cache)


    def parse_categories(self, categories):
        """
        Example response:
        u'categories': [{u'category': {u'id': 1, u'title': u'Help Needed'}}],

        Full category list 
        {"categories":[
            {"category":{"id":"1","parent_id":"0","title":"Help Needed","description":"For help required in any region.","color":"d60060","position":"0","icon":""},"translations":[]},
            {"category":{"id":"14","parent_id":"0","title":"Suppliers","description":"Suppliers of various materials","color":"48CF63","position":"0","icon":""},"translations":[]},
            {"category":{"id":"7","parent_id":"0","title":"Donation Required","description":"Those who need donation to buy supply goods","color":"cc0202","position":"1","icon":""},"translations":[]},
            {"category":{"id":"2","parent_id":"0","title":"Help Offered","description":"Help offered by volunteers in different regions","color":"008c00","position":"2","icon":""},"translations":[]},
            {"category":{"id":"9","parent_id":"0","title":"Donation Available","description":"Those who have funds to help","color":"91eda3","position":"3","icon":""},"translations":[]},
            {"category":{"id":"10","parent_id":"0","title":"Others","description":"From different sources","color":"e6841c","position":"4","icon":""},"translations":[]},
            {"category":{"id":"4","parent_id":"0","title":"Trusted Reports","description":"Reports from trusted reporters","color":"339900","position":"5","icon":""},"translations":[]},
            {"category":{"id":"6","parent_id":"0","title":"Notice","description":"This is to provide important notice.","color":"5f00ed","position":"6","icon":""},"translations":[]},
            {"category":{"id":"11","parent_id":"0","title":"Missing Reports","description":"Person Missing due to the earthquake","color":"4F444F","position":"7","icon":""},"translations":[]}
        ]}
        """
        return categories
    
    def parse_custom_fields(self, custom_fields):
        return custom_fields

    def find_record(self, row, db):
        return True 

