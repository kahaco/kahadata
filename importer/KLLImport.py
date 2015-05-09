import UshahidiImport

class KLLImport(UshahidiImport.UshahidiImport):

    def grab_data(self, use_cache=False):
        return self._grab_data('http://quakemap.org/api?task=incidents', 'kll-data.json', use_cache)

    def find_record(self, row, db):
        return True 

