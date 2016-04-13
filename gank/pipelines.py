# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

import json

class GankPipeline(object):
    # def __init__(self):
    #     self.file = open('gank.json', 'wb')

    def process_item(self, item, spider):
        print 'Start Process'
        # line = json.dumps(dict(item)) + "\n"
        # self.file.write(line)
        if item['title']:
            print item['title']
            # print item['images']
            # print item['leftLink']
            # print item['rightLink']
        else:
            raise DropItem('Missing title in %s' % item)

        # todo do what do you want!
        return item

    def open_spider(self, spider):
        print 'Open Spider'

    def close_spider(self, spider):
        print 'Close Spider'

    # def from_crawler(cls, crawler):
    #     print 'From Crawler'
    #     return cls
