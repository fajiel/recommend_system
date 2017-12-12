import scrapy
import json
import urllib
from douban.items import DoubanItem
from douban.util import TYPE_SETTINGS
class DoubanSpider(scrapy.Spider):
    name = "movie_douban"
    start_urls = [
        'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start=0&limit=50'.format(type_id) for type_id in TYPE_SETTINGS.keys()
    ]

    def parse(self, response):
        url = response.url
        args = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(args.query, True)
        type_num = params.get('type')
        if len(type_num) == 0:
            return
        movie_type = TYPE_SETTINGS.get(type_num[0])
        element_list = json.loads(response.body)
        for element in element_list:
            item = DoubanItem()
            item['title'] = element.get('title')
            item['type_num'] = type_num[0]
            item['movie_type'] = movie_type
            item['types'] = '|'.join(element.get('types')) if type(element.get('types'))is list else element.get('types')
            item['regions'] = '|'.join(element.get('regions')) if type(element.get('regions'))is list else element.get('regions')
            item['url'] = element.get('url')
            item['score'] = element.get('score')
            item['vote_count'] = str(element.get('vote_count')) if element.get('vote_count') else ''
            item['mid'] = element.get('id')
            item['release_date'] = element.get('release_date')
            item['rank'] = str(element.get('rank')) if element.get('rank') else ''
            yield item