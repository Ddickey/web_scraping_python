# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:27:51 2020

@author: Jerimiah
"""

 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#section  1
import scrapy

#section 2

class FirstSpider(scrapy.Spider):
    name = "samsung"
    start_urls = [
        
        "https://seller.samsungapps.com/login/signIn.as",

        
    ]


    def parse(self, response):
        page  = response.url.split('/')[-2]
        filename = 'samsung-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)