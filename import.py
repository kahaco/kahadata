import argparse
from kaha.bootstrap import db 

import sys
from pprint import pprint

from importer import KahaImport

def run_import(args):
    _importer = None 
    if args.source == 'kaha':
        _importer = KahaImport.KahaImport()
    else:
        raise Exception('Importer not recognized')

    rows = _importer.grab_data()
    count = 0
    failed = 0
    for r in rows:
        try:
            count = count + 1
            row = _importer.transform_row(r)
            pprint(row)
            if (not _importer.find_record(row, db)):
                db.session.add(row)
                db.session.commit()
            else:
                print "\nRecord exists"
        except:
            failed = failed + 1
            db.session.rollback()
            print "Unexpected error:", sys.exc_info()[0]
            raise
    print "\nImported: %s\nFailed to import: %s" % (count, failed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import data to Kaha')
    parser.add_argument('--s', dest='source', metavar='source', help='specify your data source')

    args = parser.parse_args()
    print args.source
    run_import(args)
