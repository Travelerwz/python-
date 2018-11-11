# -*- coding: utf-8 -*-
import scrapy
from zimuku.items import ZimukuItem

class ZimuSpider(scrapy.Spider):
    name = 'zimu'
    allowed_domains = ['zimuku.cn']
    start_urls = ['http://zimuku.cn/']

    def parse(self, response):
        '''
        :param response: 解析网页返回的内容
        :return:
        '''
        name = response.xpath("/html/body/div[2]/div/div/div[2]/table/tbody/tr[1]/td[1]/a/b/text()").extract()
     #   print(name)
        item = {}
        item['text'] = name
        yield item

