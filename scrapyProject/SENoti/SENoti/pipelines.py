# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time

class SenotiPipeline(object):
    def process_item(self, item, spider):
        now = time.strftime('%Y-%m-%d',time.localtime())
        fileName = 'SE'+now+'.txt'
        with open(fileName,'a') as fp:
            fp.write(item['serialNum'][0].encode('utf-8') + '\t')
            fp.write(item['notiName'][0].encode('utf-8') + '\t')
            fp.write(item['date'][0].encode('utf-8') + '\n\n')
        return item
