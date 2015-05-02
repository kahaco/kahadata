import re
from marshmallow import Schema, fields, ValidationError

def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')

class KahaResourceSchema(Schema):
    active  = fields.Boolean(attribute='is_active')
    contactnumber = fields.Method('format_contactnumber')
    created = fields.DateTime()
    updated = fields.DateTime()
    types = fields.Nested('KahaResourceTypeSchema', many=True, exclude=('resource',))
    stats = fields.Nested('KahaResourceStatSchema', many=True, exclude=('resource',))

    def format_contactnumber(self, resource):
        try:
            return [int(d) for d in re.split('\s|,', resource.contactnumber)]
        except ValueError:
            return None

    class Meta:
        fields = ('resource_id',
                'uuid',
                'title', 
                'district',
                'tole',
                'description',
                'contactname',
                'contactnumber',
                'updated',
                'created',
                'types',
                'stats'
                )

class KahaResourceTypeSchema(Schema):
    resource = fields.Nested(KahaResourceSchema)
    class Meta:
        fields = (
                'resource_type',
                'resource',
                )

class KahaResourceStatSchema(Schema):
    resource = fields.Nested(KahaResourceSchema)
    class Meta:
        fields = (
                'key',
                'value',
                'resource',
                )

