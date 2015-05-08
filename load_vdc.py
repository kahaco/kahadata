import json
from alembic import op

from kaha.models import db, KahaDistrict 

with open('./vdc_codes.json') as vdc_code:
    raw_data = json.load(vdc_code)

    for d in raw_data['data']:
        district = KahaDistrict(
            region=d['Region'],
            district=d['District'],
            district_code=d['District_code'],
            vdc_name=d['VDC_name'],
            vdc_code=d['VDC_code']
        )

        db.session.add(district)
        db.session.commit()
