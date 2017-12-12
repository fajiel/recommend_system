# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from douban.models import Douban, db_connect
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db_connect())
session = Session()

class DoubanPipeline(object):
    def process_item(self, item, spider):
        instance = Douban(**item)
        session.add(instance)
        try:
            session.commit()
        except Exception as e:
            print(e, '==== error in DoubanPipeline ====')
            session.rollback()
        session.close()

