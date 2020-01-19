# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:00:34 2019

@author: Jack
"""

from pandas import DataFrame
import pandas as pd
import webscraping
def getIbIndexWeights(scrape_values = False):
    if scrape_values:
        webscraping.scrapeWeights()
    df = pd.read_excel('ibIndexWeights.xlsx',sheet_name = 'sheet1')
    names = df['Aktie'].tolist()
    weights = df['Viktning'].tolist()
    prices = df['Pris'].tolist()
    return names,weights,prices