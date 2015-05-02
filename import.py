import argparse
from app import db 

import sys
from pprint import pprint

from importer import KahaImport

def run_import(args):
    _importer = None 
    if args.source == 'kaha':
        _importer = KahaImport.KahaImport()
    else:
        raise Exception('Importer not recognized')

    _importer.grab_data()
    rows = _importer.transform()
    for r in rows:
        try:
            pprint(r)
            db.session.add(r)
            db.session.commit()
        except:
            db.session.rollback()
            print "Unexpected error:", sys.exc_info()[0]



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import data to Kaha')
    parser.add_argument('--s', dest='source', metavar='source', help='specify your data source')

    args = parser.parse_args()
    print args.source
    run_import(args)
