# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GankPageItem(scrapy.Item):
    title = scrapy.Field()
    images = scrapy.Field()
    leftLink = scrapy.Field()
    rightLink = scrapy.Field()
