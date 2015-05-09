import UshahidiImport

class SparrowImport(UshahidiImport.UshahidiImport):

    def grab_data(self, use_cache=False):
        return self._grab_data('http://help.sparrowsms.com/api?task=incidents', 'sparrowsms-data.json', use_cache)

    def find_record(self, row, db):
        return True 

