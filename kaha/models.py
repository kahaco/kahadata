from sqlalchemy import Column, Integer, String, Boolean, DateTime, text, ForeignKey, PrimaryKeyConstraint, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from datetime import datetime

from bootstrap import db


class KahaDistrict(db.Model):
    """
    Region": "Eastern Region",
    District": "Taplejung",
    District_code": "1",
    VDC_name": "Ambegudin",
    VDC_code": "1001"
    """
    __tablename__ = 'kaha_location';
    __table_args__= (
            Index('district_name_idx', 'district'),
            Index('district_vdc_idx', 'vdc_name'),
            )
    location_id = Column(Integer, primary_key=True, autoincrement=True)
    region = Column(String(200))
    district = Column(String(200))
    district_code = Column(Integer)
    vdc_name = Column(String(250))
    vdc_code = Column(Integer(), unique=True)
    resources = relationship('KahaResource', backref='location')


class KahaResource(db.Model):
    __tablename__ = 'kaharesource'
    __table_args__ = (
            Index('created_kr_idx', 'created'),
            Index('updated_kr_idx', 'updated'),
            Index('district_kr_idx', 'district'),
            )

    resource_id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(50), unique=True)
    resource_for = Column(String(10))
    title = Column(String(500))
    district = Column(String(150))
    district_code = Column(Integer())
    vdc_code = Column(Integer())
    tole = Column(String(150))
    contactname = Column(String(200))
    contactnumber = Column(String(100))
    description = Column(String)
    is_active = Column(Integer)
    is_deleted = Column(Integer)
    location_id = Column(Integer, ForeignKey('kaha_location.location_id'))
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.utc_timestamp())
    data_source = relationship('KahaResourceSource', backref='resource', lazy='dynamic')
    props = relationship('KahaResourceProperty', backref='resource', lazy='dynamic')
    types = relationship('KahaResourceType', backref='resource', lazy='dynamic')


class KahaResourceSource(db.Model):
    __tablename__ = 'kaharesource_source'
    __table_args__ = (
            Index('resource_source_idx', 'source'),
            )

    resource_id = Column(Integer, ForeignKey('kaharesource.resource_id'))
    source_id = Column(String(100), primary_key=True)
    source = Column(String(20), primary_key=True)
    source_json = Column(String(500))


class KahaResourceType(db.Model):
    __tablename__ = 'kaharesource_type'
    __table_args__ = (
            Index('resource_type_idx', 'resource_type'),
            )
    id = Column(Integer, primary_key=True, autoincrement=True)
    resource_type = Column(String(100))
    resource_id = Column(Integer, ForeignKey('kaharesource.resource_id'))


class KahaResourceProperty(db.Model):
    __tablename__ = 'kaharesource_property'
    __table_args__ = (
            Index('resource_key_idx', 'key'),
            Index('created_prop_idx', 'created'),
            Index('updated_prop_idx', 'updated'),
            )

    resource_id = Column(Integer, ForeignKey('kaharesource.resource_id'), primary_key=True)
    key = Column(String(50), primary_key=True)
    value = Column(String(50))
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.utc_timestamp())
