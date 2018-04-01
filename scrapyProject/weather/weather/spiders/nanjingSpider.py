# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class NanjingspiderSpider(scrapy.Spider):
    name = 'nanjingSpider'
    allowed_domains = ['weather.com.cn']
    start_urls = ['http://www.weather.com.cn/weather/101190101.shtml']

    def parse(self, response):
        subSelector = response.xpath('//li[@class="sky skyid lv3"]') + response.xpath('//li[@class="sky skyid lv2"]')
        items = []
        for sub in subSelector:
            item = WeatherItem()
            cityDates = ''
            for cityDate in response.xpath('//div[@class="crumbs fl"]').xpath('.//text()').extract():
                cityDates += cityDate
            item['cityDate'] = cityDates

            item['week'] = sub.xpath('./h1//text()').extract()[0]
            temps = ''
            for temp in sub.xpath('./p[2]//text()').extract():
                temps += temp
            item['temperature'] = temps
            item['weather'] = sub.xpath('./p[1]//text()').extract()[0]
            item['wind'] = sub.xpath('./p[3]/i//text()').extract()[0]
            items.append(item)
        return items
