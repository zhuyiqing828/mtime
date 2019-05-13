# -*- coding:utf-8 -*-

import scrapy
from doubanurl.items import DoubanurlItem
import jsonlines
import json
import requests
import time

def read_url(url):
    #按行读取json文件 读取json文件中的http的关键字，存入url数组中
    with open("tencent_film.json", encoding='utf-8') as f:
        for line in jsonlines.Reader(f):
            title = line['title']
            if title:
                url.append("https://www.baidu.com/s?tn=80035161_2_dg&wd="+title+" 豆瓣电影")
            else:
                url.append("没有标题，无法取得url")
    return 1
#
# class DoubanSpider(scrapy.Spider):
#     name = "doubanurl"                                   #scrapy crawl douban -o items.json
#     #allowed_domains = ["movie.douban.com"]
#     next_url = []
#     read_url(next_url)  #把所有百度要搜索的url读入保存到next_url数组中
#
#     def start_requests(self):
#         for i in range(0, len(self.next_url)):
#             item = DoubanurlItem()
#             item['index'] = i+1
#             item['url'] = self.next_url[i]
#             #print(self.next_url[i])
#             yield scrapy.Request(self.next_url[i], meta={'item': item}, callback=self.parse, dont_filter=True)
#
#     def parse(self, response):
#         for sel in response.xpath('/html'):
#             item = response.meta['item']
#             baidu_url = sel.xpath('//*[@id="1"]/h3/a/attribute::href').extract()
#             print("!!!!!!!!!!!!!!")
#             item['doubanurl_url'] = (baidu_url[0])
#             yield item

# -*- coding: utf-8 -*-


################################重新爬取第一轮结果中 异常的条目的豆瓣真实url
import scrapy
from scrapy.conf import settings
from scrapy.http.response.html import HtmlResponse
from scrapy.http import Request
from scrapy.http.cookies import CookieJar

def bdurlCode(url):                                  #提取跳转链接
    res = requests.get(url, allow_redirects=False)
    real_url = res.headers['location']
    return real_url

class DoubanSpider(scrapy.Spider):
    name = "doubanurl"
    next_url = []
    read_url(next_url)  #把所有百度要搜索的url读入保存到next_url数组中
    with open("items_abnormal.json", encoding='utf-8') as f:
        abnormal_items = json.load(f)

    def start_requests(self):
        count = 0
        for abnormal_item in self.abnormal_items:
            # count += 1
            # if count >= 2:
            #     break
            item = DoubanurlItem()
            item["index"] = abnormal_item["douban_index"]
            baidu_url = self.next_url[abnormal_item["douban_index"]-1]
            item["baidu_search"] = baidu_url
            print(baidu_url)
            if baidu_url != "没有标题，无法取得url":
                yield scrapy.Request(baidu_url, meta={'item': item}, callback=self.baidu_search, dont_filter=True)

    def baidu_search(self, response):              #通过百度搜索获得豆瓣跳转链接
        for sel in response.xpath('/html'):
            item = response.meta['item']
            baidu_jump_url = sel.xpath('//*[@id="1"]/h3/a/attribute::href').extract()
            print("get baidu_jump_url ")
            print(baidu_jump_url[0])

            item["douban_real_url"] =bdurlCode(baidu_jump_url[0])

            yield item
