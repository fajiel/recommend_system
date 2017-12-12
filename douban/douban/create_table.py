from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

def db_connect():
    return create_engine('mysql+mysqlconnector://root:''@localhost:3306/recommend_system?charset=utf8', echo=False)

Base = declarative_base()

class Tmp(Base):
    __tablename__ = 'douban_movie'
    __table_args__ =(
     {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    })

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(128), nullable=False)
    movie_type = Column(String(128), nullable=False)
    type_num = Column(String(30), nullable=False)
    types = Column(String(30), nullable=False)
    regions = Column(String(32))
    url = Column(String(128))
    score = Column(String(32))
    vote_count = Column(String(64))
    mid = Column(String(64))
    release_date = Column(String(32))
    rank = Column(String(8))


if __name__ =='__main__':
    import os
    import logging
    from datetime import datetime

    dirpath = os.getcwd()
    datestr = datetime.strftime(datetime.now(), '%Y-%m-%d_%H')
    logger = logging.getLogger('')
    hdlr = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

    try:
        Base.metadata.create_all(db_connect())
    except Exception:
        logging.exception('create failed')
    else:
        logging.info('created')
