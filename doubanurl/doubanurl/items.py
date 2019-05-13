# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanurlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    douban_real_url = scrapy.Field()
    index = scrapy.Field()
    baidu_search = scrapy.Field()


    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
