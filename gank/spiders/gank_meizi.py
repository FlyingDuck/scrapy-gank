# -*- coding: utf-8 -*-
__author__ = 'dongsj'

import scrapy

from scrapy.spider import Spider
from scrapy.selector import Selector

from gank.items import GankMeizi

class GankMeiZiSpider(Spider):
    name = 'gankMeiZi'
    allowed_domains = ["gank.io"]
    start_urls = [
        "http://gank.io"
    ]

    def parse(self, response):
        """
            用来爬取http://gank.io 妹子图片
        """
        base_url = 'http://gank.io'
        sel = Selector(response)
        # 页面标题
        title = sel.xpath("//div[@class='typo']/div/h1/text()").extract()
        # 图片
        image = sel.xpath("//div[@class='outlink']/h1/img/@src").extract()
        # 前一页面地址
        refs = sel.xpath("//div[@class='typo']/div[@class='container content']/div[@class='row'][1]/div[@class='six columns']/p/a/@href").extract()

        # Item 对象
        meizi = GankMeizi()
        meizi['title'] = title[0]
        meizi['image'] = image[0]
        meizi['refs'] = refs

        yield meizi

        if 0 < len(refs):
            url = base_url + refs[0]
            yield scrapy.Request(url, callback=self.parse)
