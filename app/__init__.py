__author__ = 'maddalena'


# -----------------------------------------------------------------------
# SQLAlchemy
# -----------------------------------------------------------------------
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI
engine = create_engine(SQLALCHEMY_DATABASE_URI)     # the database engine
Session = sessionmaker(bind=engine)                 # create the Session class
modelbase = declarative_base()                      # the model base object


# -----------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------
# import logging
# from logging.handlers import RotatingFileHandler
# logger = logging.getLogger('mylog')
# logger.setLevel(logging.DEBUG)
# file_handler = RotatingFileHandler('tmp/alchemy.log', 'a', 1 * 1024 * 1024, 10)
# file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s [in %(pathname)s:%(lineno)d]'))
# file_handler.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)
# logger.info('application startup')


# -----------------------------------------------------------------------
# Logging with config file
# -----------------------------------------------------------------------
import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger('myLog')
logger.info('application startup')