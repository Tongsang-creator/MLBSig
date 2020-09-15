import numpy as np
import csv
import math
import random
# save numpy array as csv file
from numpy import asarray
from numpy import savetxt
from numpy import loadtxt
def float_ceil(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

def float_floor(a,b):
    return (a*10//b)/10
sell_price = {}
sell_price_count = 0
buy_price = {}
buy_price_count = 0

with open('AUD_JPY_price.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        sell_price[sell_price_count] =  row["sell price"]
        sell_price_count += 1
        buy_price[buy_price_count] =  row["buy price"]
        buy_price_count += 1
        #print(f'\t{row["bar#"]} : {row["buy price"]}, {row["sell price"]}, {row["volume"]}, {row["close"]}, {row["open"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')

zone = np.arange(60.0, 90.1, 0.1)
zone_status_buy = {}
zone_status_sell = {}
best_Y = np.zeros(30000)
best_cf = 0
n = 1
datamax = 1000
datacount = 1

for iterator in range(0,n):
#innitial
    Y = np.zeros(30000)
    cf_unreal = 0
    cf_real = 0
    last_price = 0.0
    last_buy = 90.0
    for i in zone:
        #zone_status_buy[str(round(i,1))] = 1
        zone_status_sell[str(round(i+0.1,1))] = 0

    #for i in range(0,30000):
    Y = data = loadtxt('data.csv', delimiter=',')
        #Y[i] = 1 #58.304999999986464
#run
    for i in range(0,sell_price_count):
        if i == 0:
            last_price = float_floor(float(sell_price[i]),1)
        else:
            if float_floor(float(sell_price[i]),1) <= 90.1 and float_floor(float(sell_price[i]),1) >= 60.1:
                for j in np.arange(last_price,float_floor(float(sell_price[i]),1),0.1):
                    cf_unreal += zone_status_sell[str(float_floor(float(sell_price[i]),1))]
                    zone_status_sell[str(float_floor(float(sell_price[i]),1))] = 0  
            last_price = float_floor(float(sell_price[i]),1)
#trade      
        if Y[i] == 1:
            cf_real += cf_unreal
            cf_unreal = 0
            if float_floor(float(sell_price[i]),1) <= 90.1 and float_floor(float(sell_price[i]),1) >= 60.1:
                for j in np.arange(float_floor(float(sell_price[i]),1), 90.0, 0.1):
                    if zone_status_sell[str(round(j,1))] == 0:
                        zone_status_sell[str(round(j,1))] = np.maximum(j - float(buy_price[i]),0)
                    else:
                        break
        #if float(sell_price[i]) >= 60.0 and float(sell_price[i]) <= 90.1:   
        #    zone_status_sell[str(float_floor(float(sell_price[i]),1))] = 0
        #    zone_status_buy[str(float_floor(float(sell_price[i])-0.1,1))] = 0
#summary
    if cf_real > best_cf:
        best_Y = np.copy(Y)
        best_cf = cf_real
        # save to csv file
        path = "D:\\Completation\\MLBSig\data\\" + "data" +  str(datacount) + ".csv"
        savetxt(path, best_Y, delimiter=',')
        datacount+=1
        if datacount > datamax:
            datacount = 0

    print(f'iterator = {iterator+1} cf_real = {cf_real} best = {best_cf}')


