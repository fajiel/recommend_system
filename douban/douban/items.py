# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    movie_type = scrapy.Field()
    type_num = scrapy.Field()
    types = scrapy.Field()
    regions = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    vote_count = scrapy.Field()
    mid = scrapy.Field()
    release_date = scrapy.Field()
    rank = scrapy.Field()
    property = scrapy.Field()