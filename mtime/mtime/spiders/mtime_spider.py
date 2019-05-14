# -*- coding:utf-8 -*-

import scrapy
from mtime.items import MtimeItem
import jsonlines
import requests
import time
import json
# from bs4 import beautifulsoup

def read_url(url):
    #按行读取json文件 读取json文件中的http的关键字，存入url数组中
    with open("tencent_film.json", encoding='utf-8') as f:
        for line in jsonlines.Reader(f):
            title = line['title']
            if title:
                url.append("https://www.baidu.com/s?tn=80035161_2_dg&wd="+title+" Mtime时光网")
            else:
                url.append("没有标题，无法取得url")
    return 1


def bdurlCode(url):                                  #提取跳转链接
    res = requests.get(url, allow_redirects=False)
    real_url = res.headers['location']
    return real_url


class DoubanSpider(scrapy.Spider):
    name = "mtime"                                   #scrapy crawl douban -o items.json
    #allowed_domains = ["movie.douban.com"]
    next_url = []
    read_url(next_url)  #把所有豆瓣的url（百度跳转链）读入保存到next_url数组中

    def start_requests(self):
        count = 0
        for i in range(0, len(self.next_url)):
            item = MtimeItem()
            count += 1
            item["index"] = i + 1
            item["baidu_url"] = self.next_url[i]
            if count >= 486:
                yield scrapy.Request(self.next_url[i], meta={'item': item}, callback=self.baidu_search, dont_filter=True)

    def baidu_search(self, response):  # 通过百度搜索获得豆瓣跳转链接
        for sel in response.xpath('/html'):
            item = response.meta['item']
            baidu_jump_url = sel.xpath('//*[@id="1"]/h3/a/attribute::href').extract()

            item["mtime_url"] = bdurlCode(baidu_jump_url[0])

            yield item

