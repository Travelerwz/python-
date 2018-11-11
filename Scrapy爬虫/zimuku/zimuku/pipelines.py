# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZimukuPipeline(object):
    def process_item(self, item, spider):
        with open("F:\\python\\1.txt", 'a') as fp:
            fp.write(str(item['text']))
        print(item['text'])

