import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BRAND_NAME = 'CODES'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PROD_SQLALCHEMY_DATABASE_URI') or 'mysql://root:root@localhost/my_codes_db'


class DevelopmentConfig(Config):
    DEBUGGING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_SQLALCHEMY_DATABASE_URI') or 'mysql://root:root@localhost/my_codes_db'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_SQLALCHEMY_DATABASE_URI') or 'mysql://root:root@localhost/my_codes_db'


config = {'production': 'config.ProductionConfig',
          'development': 'config.DevelopmentConfig',
          'test': 'config.TestConfig'}
