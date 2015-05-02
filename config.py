import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('KAHA_SECRET', 'xxxx')
    SQLALCHEMY_DATABASE_URI = os.getenv('KAHA_DSN', 'xxx')
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
