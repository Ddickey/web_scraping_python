# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:25:59 2020

@author: Jerimiah
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


#r = requests.get('https://www.amazon.com/Best-Sellers/zgbs')

def review_count_scrape():
    url = 'https://www.amazon.com/Best-Sellers/zgbs'
    headers = ({'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'})
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.status_code)
    product_total_review = [i.text for i in soup.findAll('a', {'class': 'a-size-small a-link-normal'})]
    df = pd.DataFrame(product_total_review)
    print(df)
    
    #adding a timer 
    time.sleep(60)
    
end_timer = time.time() + 60 * 2 
while time.time() < end_timer:
    review_count_scrape()