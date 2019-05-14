# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozItem(scrapy.Item):
    tencent_index = scrapy.Field()
    #tencent_title = scrapy.Field()
    tencent_keywords = scrapy.Field()
    #tencent_cover_image_url = scrapy.Field()
    #tencent_link = scrapy.Field()
    tencent_movie_tags = scrapy.Field()
    #tencent_information = scrapy.Field()
    tencent_douban_IMBD_M_score = scrapy.Field()
    tencent_play_num = scrapy.Field()
    tencent_content_location = scrapy.Field()
    #tencent_support_rate = scrapy.Field()
