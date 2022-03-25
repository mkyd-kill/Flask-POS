from dotenv import load_dotenv
import os
from pub import DB_NAME
from pub.validators import secretKey

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = secretKey()
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, DB_NAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEVELOPMENT = False
    DEBUG = False

class StagingConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TESTING = True