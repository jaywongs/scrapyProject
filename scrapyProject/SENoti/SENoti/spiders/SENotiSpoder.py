# -*- coding: utf-8 -*-
import scrapy
from SENoti.items import SenotiItem

class SenotispoderSpider(scrapy.Spider):
    name = 'SENotiSpoder'
    allowed_domains = ['software.nju.edu.cn']
    start_urls = ['http://software.nju.edu.cn/index.php?option=com_content&view=category&id=66&Itemid=12']

    def parse(self, response):
        subSelector = response.xpath('//tr[@class="sectiontableentry1"]') #嵌套选择
        items = []
        for sub in subSelector:
            item = SenotiItem()
            item['notiName'] = sub.xpath('./td/text()').extract()
            items.append(item)
        return items

