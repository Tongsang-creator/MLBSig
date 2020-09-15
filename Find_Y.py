import numpy as np
import csv
import math
import random
# save numpy array as csv file
from numpy import asarray
from numpy import savetxt

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
n = 10000


for iterator in range(0,n):
#innitial
    Y = np.zeros(30000)
    cf = {}
    for i in zone:
        zone_status_buy[str(round(i,1))] = 1
        zone_status_sell[str(round(i+0.1,1))] = 1
        cf[str(round(i,1))] = 0
    for i in range(0,30000):
        Y[i] = random.randint(0,1)   
#run
    for i in range(0,sell_price_count):
        if Y[i] == 1:
            for j in np.arange(float_ceil(float(buy_price[i]),1), 90.0, 0.1):
                if(zone_status_buy[str(round(j,1))] == 0) :
                    cf[str(round(j,1))] += 1
                zone_status_sell[str(round(j,1))] = 1
        if float(sell_price[i]) >= 60.0 and float(sell_price[i]) <= 90.1:
            zone_status_sell[str(float_floor(float(sell_price[i]),1))] = 0
            zone_status_buy[str(float_floor(float(sell_price[i])-0.1,1))] = 0
        
#summary cf
    sum_cf = 0
    for i in cf:
        sum_cf += cf[i]
    if sum_cf > best_cf:
        best_Y = np.copy(Y)
        best_cf = sum_cf
        # save to csv file
        savetxt('data.csv', best_Y, delimiter=',')

    print(f'iterator = {iterator+1} sum_cf = {sum_cf} best = {best_cf}')


