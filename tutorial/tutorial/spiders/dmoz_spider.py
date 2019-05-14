# -*- coding:utf-8 -*-
import scrapy

import scrapy
from tutorial.items import DmozItem
import jsonlines


def read_url(url):
    #按行读取json文件 读取json文件中的http的关键字，存入url数组中
    with open("tencent_film.json", encoding='utf-8') as f:
        for line in jsonlines.Reader(f):
            url_key = line['coverId']
            url.append("https://v.qq.com/x/cover/"+url_key+".html")
    return 1

class DmozSpider(scrapy.Spider):
    handle_httpstatus_list = [404]
    name = "dmoz"
    allowed_domains = ["v.qq.com"]
    next_url = []
    read_url(next_url)  #把所有url读入保存到next_url数组中
    print(len(next_url))

    def start_requests(self):
        for i in range(3618, len(self.next_url)):
            item = DmozItem()
            item['tencent_index'] = i+1
            yield scrapy.Request(self.next_url[i], meta={'item': item}, callback=self.parse, dont_filter=True)


    def parse(self, response):
        for sel in response.xpath('/html'):
            item = response.meta['item']
            #item['tencent_information'] = sel.xpath('//script[@type="text/javascript"]/attribute::content').extract()
            #item['movie_title'] = sel.xpath('//title/text()').extract()
            item['tencent_keywords'] = sel.xpath('//meta[@name="keywords"]/attribute::content').extract()
            #item['tencent_cover_image_url'] = sel.xpath('//meta[@itemprop="image"]/attribute::content').extract()
            item['tencent_movie_tags'] = sel.xpath('//div[@class="video_tags _video_tags"]//a/text()').extract()
            item['tencent_douban_IMBD_M_score'] = sel.xpath('//span[@class="video_score"]//span[@class="num"]/text()').extract()
            item['tencent_keywords'] = sel.xpath('//meta[@name="keywords"]/attribute::content').extract()
            item['tencent_play_num'] = sel.xpath('//*[@id="mod_cover_playnum"]/text()').extract()
            item['tencent_content_location'] = sel.xpath('/html/head/meta[@itemprop="contentLocation"]/attribute::content').extract()
            yield item

