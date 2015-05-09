import argparse
from kaha.bootstrap import db 
from kaha.models import KahaDistrict

import sys
import uuid
from pprint import pprint

from importer import KahaImport

def run_import(args):
    _importer = None 
    if args.source == 'kaha':
        _importer = KahaImport.KahaImport()
    else:
        raise Exception('Importer not recognized')

    rows = _importer.grab_data(True)
    skipped = 0
    count = 0
    failed = 0
    for r in rows:
        try:
            row = _importer.transform_row(r)

            if (not _importer.find_record(r, db)):
                row.uuid = str(uuid.uuid4())
                vdc = db.session.query(KahaDistrict).filter_by(vdc_name=row.tole).first()
                if vdc:
                    row.district = vdc.district
                    row.district_code = vdc.district_code
                    row.vdc_code = vdc.vdc_code
                else:
                    district = db.session.query(KahaDistrict).filter_by(district=row.district).first()
                    if district:
                        row.district_code = district.district_code

                db.session.add(row)
                db.session.commit()
                count = count + 1
            else:
                skipped = skipped + 1
                print "\nRecord exists"
        except:
            failed = failed + 1
            db.session.rollback()
            print "Unexpected error:", sys.exc_info()[0]
            raise
    print "\nImported: %s\nSkipped: %s\nFailed to import: %s" % (count, skipped, failed)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Import data to Kaha')
    parser.add_argument('--s', dest='source', metavar='source', help='specify your data source')

    args = parser.parse_args()
    print args.source
    run_import(args)
