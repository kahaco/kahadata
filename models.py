from app import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime, text, ForeignKey,PrimaryKeyConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from datetime import datetime
import json
from json import JSONDecoder, JSONEncoder

class DateTimeDecoder(JSONDecoder):
 
    def __init__(self, *args, **kargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object,
                             *args, **kargs)
    
    def dict_to_object(self, d): 
        if '__type__' not in d:
            return d
 
        type = d.pop('__type__')
        try:
            dateobj = datetime(**d)
            return dateobj
        except:
            d['__type__'] = type
            return d
 
class DateTimeEncoder(JSONEncoder):
    """ Instead of letting the default encoder convert datetime to string,
        convert datetime objects into a dict, which can be decoded by the
        DateTimeDecoder
    """
        
    def default(self, obj):
        if isinstance(obj, datetime):
            return {
                '__type__' : 'datetime',
                'year' : obj.year,
                'month' : obj.month,
                'day' : obj.day,
                'hour' : obj.hour,
                'minute' : obj.minute,
                'second' : obj.second,
                'microsecond' : obj.microsecond,
            }   
        else:
            return JSONEncoder.default(self, obj)

def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    convert = dict()
    # add your coversions for things like datetime's 
    # and what-not that aren't serializable.
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if c.type in convert.keys() and v is not None:
            try:
                d[c.name] = convert[c.type](v)
            except:
                d[c.name] = "Error:  Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d, cls=DateTimeEncoder)

class KahaResource(db.Model):
    __tablename__ = 'kaharesource'
    __table_args__ = (Index('created_kr_idx', 'created'), Index('updated_kr_idx', 'updated'),)

    resource_id = Column(Integer, primary_key=True)
    uuid = Column(String(50), unique=True)
    title = Column(String(500))
    district = Column(String(150))
    tole = Column(String(150))
    contactname = Column(String(200))
    contactnumber = Column(String(100))
    description = Column(String)
    is_active = Column(Integer)
    is_deleted = Column(Integer)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.utc_timestamp())
    types = db.relationship('KahaResourceType', backref='resource',
                                    lazy='dynamic')
    stats = relationship("KahaResourceStat", backref="kaharesource", lazy='dynamic')

    @property
    def json(self):
        return to_json(self, self.__class__)


class KahaResourceType(db.Model):
    __tablename__ = 'kaharesource_type'

    id = Column(Integer, primary_key=True)
    resource_type = Column(String(100))
    resource_id = Column(Integer, ForeignKey('kaharesource.resource_id'))

    #resource = relationship("KahaResource", back_populates="types")


class KahaResourceStat(db.Model):
    __tablename__ = 'kaharesource_stat'
    __table_args__ = (Index('created_ks_idx', 'created'), Index('updated_ks_idx', 'updated'),)

    key = Column(String(20), primary_key=True)
    resource_id = Column(Integer, ForeignKey('kaharesource.resource_id'), primary_key=True)
    value = Column(Integer)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.utc_timestamp())

    #resource = relationship("KahaResource", back_populates="stats")
