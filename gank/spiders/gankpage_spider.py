# -*- coding: utf-8 -*-

import scrapy

from gank.items import GankPageItem


class GnakPageSpider(scrapy.Spider):
    name = "gank"
    allowed_domains = ["gank.io"]
    start_urls = [
        "http://gank.io",
    ]
    url_prefix = "http://gank.io"

    def parse(self, response):

        pageItem = self.extract_item(response)
        yield pageItem

        # 左部导航不为空 则向左部爬取
        leftLinks = pageItem['leftLink']
        if len(leftLinks) == 1:
            leftLink = self.url_prefix + leftLinks[0]
            yield scrapy.Request(leftLink, callback=self.to_left_page)
        # 右部导航不为空 则向右部爬取
        rightLinks = pageItem['rightLink']
        if len(rightLinks) == 1:
            rightLink = self.url_prefix + rightLinks[0]
            yield scrapy.Request(rightLink, callback=self.to_right_page)

    def extract_item(self, response):
        '''
            页面解析
        '''
        selector = scrapy.Selector(response)
        tagTitle = selector.xpath('head/title')
        tagNavDivs = selector.xpath('(//div[contains(@class, "typo")]/div[contains(@class, "container content")]/div[contains(@class, "row")])[1]/div')
        tagPs = selector.xpath('//div[contains(@class, "typo")]/div[contains(@class, "container content")]/div[contains(@class, "outlink")]/p')

        pageItem = GankPageItem()
        # 页面标题
        pageTitle = tagTitle.xpath('text()').extract()[0]
        pageItem['title'] = pageTitle #.encode('utf-8')
        # 妹纸图片
        pageItem['images'] = tagPs.xpath('./img/@src').extract()
        # 导航链接
        if len(tagNavDivs) == 2:
            pageItem['leftLink'] = tagNavDivs[0].xpath('./p/a/@href').extract()
            pageItem['rightLink'] = tagNavDivs[1].xpath('./p/a/@href').extract()
        else:
            pageItem['rightLink'] = tagNavDivs[0].xpath('./p/a/@href').extract()

        return pageItem

    def to_left_page(self, response):
        '''
            左部爬取
        '''
        pageItem = self.extract_item(response)
        yield pageItem

        leftLinks = pageItem['leftLink']
        if len(leftLinks) == 1:
            leftLink = self.url_prefix + leftLinks[0]
            yield scrapy.Request(leftLink, callback=self.to_left_page)

    def to_right_page(self, response):
        '''
            右部爬取
        '''
        pageItem = self.extract_item(response)
        yield pageItem

        rightLinks = pageItem['rightLink']
        if len(rightLinks) == 1:
            rightLink = self.url_prefix + rightLinks[0]
            yield scrapy.Request(rightLink, callback=self.to_right_page)