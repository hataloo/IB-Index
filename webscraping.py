# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:54:22 2019

@author: Jack
"""
import json
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#import lxml.html as lh
import pandas as pd

import csv
from datetime import datetime
from pandas import DataFrame
def scrapeWeights():
    url = 'http://ibindex.se/ibi/#/index'
    urlWeights = 'http://ibindex.se/ibi//index/getProductWeights.req'
    urlTrends = 'http://ibindex.se/ibi//index/getTrends.req'
    urlProducts = 'http://ibindex.se/ibi//index/getProducts.req'
    
    
    page = requests.get(urlWeights)
    soup = BeautifulSoup(page.content,"html.parser")
    
    pageTrends = requests.get(urlTrends)
    soupTrends = BeautifulSoup(pageTrends.content,"html.parser")
    
    pageProducts = requests.get(urlProducts)
    soupProducts = BeautifulSoup(pageProducts.content,"html.parser")
    
    print(page,pageTrends,pageProducts)
    dataWeights = json.loads(str(soup))
    
    dataTrends = json.loads(str(soupTrends))
    
    dataProducts = json.loads(str(soupProducts))
    
    names = []
    weights = []
    prices = []
    for prod in dataWeights:
        weights.append(prod['weight']/100)
        names.append(prod['productName'])
    
    for prod in dataProducts:
        prices.append(prod['price'])
    
    
    df = DataFrame({'Aktie':names,'Viktning':weights,'Pris':prices,'Datum':datetime.now().date()})
    df.to_excel('ibIndexWeights.xlsx',sheet_name = 'sheet1',index = False)
    return
#with open('ibIndexWeights.csv','w',newline ='') as csv_file:
#with open('ibIndexWeights.xlsx',newline ='') as csv_file:

#    writer = csv.writer(csv_file)
#    for product in dataWeights:
#        writer.writerow([product['product'],product['productName'],product['weight'],datetime.now().date()])