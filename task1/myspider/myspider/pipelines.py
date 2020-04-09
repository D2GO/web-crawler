# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'indiatimes':
            print(item)
            jsonData = json.dumps(item)
            fileObject = open('../task1_data.json', 'a')
            fileObject.write(jsonData)
            fileObject.write('\n')
            fileObject.close()
            return item
        elif spider.name == 'indiatimes2':
            print(item)
            return item
