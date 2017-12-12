# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
Base = declarative_base()

def db_connect():
    return create_engine('mysql+mysqlconnector://root:''@localhost:3306/recommend_system?charset=utf8', echo=False)

class Douban(Base):
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
