# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:53:12 2020

@author: Jerimiah
"""

import scrapy
from practicalone.items import PracticaloneItem

class SecondSpider(scrapy.Spider):
    name = "Books2"
    start_urls = [
        
      "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",

        ]
    
    def parse(self, response):
        item = PracticaloneItem()
        item['title'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
        item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
        item['price'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').get()
        item['in_stock'] = response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]').extract()
        
        return item