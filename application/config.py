import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG=False
    SQLITE_DB_DIR=None
    SQLALCHEMY_DB_URL=None
    SQLALCHEMY_TRACK_MODIFICATION=False
    
class LocalDevlopmentConfig(Config):
    SQLITE_DB_DIR=os.path.join(basedir,"../db_directory")
    SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(SQLITE_DB_DIR,"projectdb.db")
    DEBUG=True
    
