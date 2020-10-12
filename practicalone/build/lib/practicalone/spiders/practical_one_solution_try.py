# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:41:50 2020

@author: Jerimiah
"""

import scrapy
from practicalone.items import PracticaloneItem
    
class SolutionSpider(scrapy.Spider):
    name = "Solution"
    #allowed_domains[]
    #only allowed domains
    start_urls = [
        
        "http://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html",
        "http://books.toscrape.com/catalogue/immunity-how-elie-metchnikoff-changed-the-course-of-modern-medicine_900/index.html",
        "http://books.toscrape.com/catalogue/tipping-point-for-planet-earth-how-close-are-we-to-the-edge_643/index.html",
        "http://books.toscrape.com/catalogue/the-grand-design_405/index.html",
        
        ]
    
    def parse(self, response):
        item = PracticaloneItem()
        item['category'] = response.xpath["ul[@class='breadcrumb']/li[3]/a/text()"].get()
        item['price'] = response.xpath["/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/p[1]"].get()
        item['title'] = response.xpath["/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1"].get()
        item['in_stock'] = response.xpath["ul[@class'instock availability']"]
        
        return