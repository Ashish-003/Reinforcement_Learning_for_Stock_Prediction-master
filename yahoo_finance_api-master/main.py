from yahoo_finance_api import YahooFinance as yf
import pandas as pd
import time
tata_power = yf('TATAPOWER.NS',result_range='1d',interval='1m').to_csv('../Reinforcement_Learning_for_Stock_Prediction-master/data/tatapower.csv','w',False)
#Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]

old= tata_power.iloc[[len(tata_power) - 1]].index.values

date2 = tata_power.iloc[[11]].index.values
i = 1
while(True):
    
    tata_power = yf('TATAPOWER.NS',result_range='5m',interval='1m').check()
    new = tata_power.iloc[[len(tata_power) - 2]].index.values
    print("\n\n\n aloo lelo\n\n\n")
    print(tata_power)
    if(new != old):
        yf('TATAPOWER.NS',result_range='1d',interval='1m').to_csv('../Reinforcement_Learning_for_Stock_Prediction-master/data/tatapower.csv','w',False)
        old = new
        time.sleep(40)
    #time.sleep(40)
    print("idk how this shit works" + str(i))
    i+=1

# tata_power = yf('TATAPOWER.NS',result_range='5m',interval='1m').to_csv('tatapower.csv','a',False)

# if(date1 != date2):
# print(tata_power)
