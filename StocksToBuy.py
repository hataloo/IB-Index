# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:33:25 2019

@author: Jack
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:02:25 2019

@author: Jack
"""
import sys,getopt,os
from argparse import ArgumentParser
#print(sys.path)
#print()
#print(os.getcwd())
sys.path.append('D:\Programmering\Anaconda\envs\Machine Learning\Lib\site-packages')
sys.path.append('D:\Programmering\Anaconda\Lib\site-packages')
import numpy as np
import pandas as pd
from pandas import DataFrame
from datetime import datetime
import getIbIndexWeights as IB
parser = ArgumentParser()
parser.add_argument("-c","--capital",type = int,dest = 'capital',help="amount of money to buy for",metavar="CAPITAL")
parser.add_argument("-s","--scrape",type = bool,dest = 'ScrapeValues',help ="Indicates whether new values are scraped.",default = False)
args = parser.parse_args()

def StocksToBuy(stocks_prior,new_capital,prices,goal_weights,courtage_rate = 0.001):
    total_capital = np.dot(stocks_prior,prices)+new_capital
    number_of_stocks_to_buy = goal_weights/prices*total_capital-stocks_prior
    number_of_stocks_to_buy  =np.round(number_of_stocks_to_buy)
    total_new_stocks = number_of_stocks_to_buy+stocks_prior
    proc_weigths = (total_new_stocks)*prices/(np.dot(total_new_stocks,prices))
    
    courtage = np.round(np.abs(number_of_stocks_to_buy)*prices*courtage_rate)
    courtage_roundup = np.less(number_of_stocks_to_buy,1) & np.not_equal(number_of_stocks_to_buy,0)
    courtage = np.sum(courtage) + np.sum(courtage_roundup)
    
    remaining_capital = new_capital - np.dot(number_of_stocks_to_buy,prices)-courtage
    
    mean_deviation = np.mean(np.abs(goal_weights-proc_weigths))
    return number_of_stocks_to_buy,proc_weigths,remaining_capital,courtage,mean_deviation

def getIbStocksToBuy(new_capital,stocks_prior = np.zeros(14),courtage_rate = 0.001,scrape_values = False):
    [names,weights,prices] = IB.getIbIndexWeights(scrape_values)
    
    weights = np.asarray(weights)
    prices = np.asarray(prices)
    
    number_of_stocks = np.max(np.shape(names))
    
    [to_buy,proc_weights,remaining_capital,courtage,mean_deviation] = StocksToBuy(stocks_prior,new_capital,prices,weights,courtage_rate)
    deviation = proc_weights - weights
    #print(to_buy)
    #print(mean_deviation)
    #print('Remaining capital:' + np.array2string(remaining_capital)+ ' at '+str(new_capital))
    #print(courtage)
    stocks_prior = stocks_prior.astype(int)
    to_buy = to_buy.astype(int)
    df = DataFrame({'Aktie':names,'Viktning':weights,'Pris':prices,'Datum':datetime.now().date(),'Nuvarande antal':stocks_prior,'Att köpa':to_buy,'Avvikelse':deviation,'Överblivet kapital':remaining_capital})
    return df


def main(args):
    new_capital = 30000
    scrape_values = False
    if args.capital is not None:
        new_capital = args.capital
    if args.ScrapeValues is not None:
        scrape_values = args.ScrapeValues
    
    df = pd.read_excel(pd.ExcelWriter('ibNuvarandeAktier.xlsx',engine = 'xlsxwriter'))
    data = getIbStocksToBuy(new_capital,stocks_prior = df['Nuvarande antal'].to_numpy(),courtage_rate = 0.001,scrape_values = scrape_values)
    #data.to_excel('ibNuvarandeAktier.xlsx',sheet_name = 'sheet1',index = False)
    writer = pd.ExcelWriter('ibNuvarandeAktier.xlsx',engine = 'xlsxwriter')
    data.to_excel(writer,sheet_name = 'sheet1',index = False)

    worksheet = writer.sheets['sheet1']
    for idx, col in enumerate(data):
        
        max_len = len(col)
        for item in data[col]:
            max_len = max(max_len,len(str(item)))
        max_len +=1
        worksheet.set_column(idx,idx,max_len)
    writer.save()
    #write.close()
    print(data)
    print(pd.__version__,sys.version)
main(args)