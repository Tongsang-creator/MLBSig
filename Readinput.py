import csv
from numpy import asarray
from numpy import savetxt
import numpy as np
import pandas as pd
#read x
test_x = {}
test_x_count = 0
train_x = {}
train_x_count = 0
data = asarray([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
with open('AUD_JPY_price.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if line_count < 9001:
            test_x[test_x_count] = [(float(row["open"])-68.86259253)/3.620579894**2,(float(row["high"])-68.8889767)/3.608828267**2,(float(row["low"])-68.83644273)/3.632035774**2,(float(row["close"])-68.86246913)/3.620495958**2,(float(row["volume"])-423.1541667)/380.0432996]
            test_x_count += 1
        else:
            train_x[train_x_count] = [(float(row["open"])-68.8889767)/3.620579894**2,(float(row["high"])-68.8889767)/3.608828267**2,(float(row["low"])-68.83644273)/3.632035774**2,(float(row["close"])-68.86246913)/3.620495958**2,(float(row["volume"])-423.1541667)/380.0432996]
            train_x_count += 1
        line_count += 1
df = pd.DataFrame(test_x)
df2 = pd.DataFrame(train_x)
df.to_csv (r'test_x.csv', index = False, header=False)
df2.to_csv (r'train_x.csv', index = False, header=False)
#read y
test_y = {}
test_y_count = 0
train_y = {}
train_y_count = 0

with open('data2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count < 9000:
            test_y[test_y_count] = row
            test_y_count += 1
        else:
            train_y[train_y_count] = row
            train_y_count += 1
        
        line_count += 1
df = pd.DataFrame(test_x)
df2 = pd.DataFrame(train_x)
df3 = pd.DataFrame(test_y)
df4 = pd.DataFrame(train_y)
df.to_csv (r'test_x.csv', index = False, header=False)
df2.to_csv (r'train_x.csv', index = False, header=False)
df3.to_csv (r'test_y.csv', index = False, header=False)
df4.to_csv (r'train_y.csv', index = False, header=False)
#array = np.array(test_x.items())
"""
with open('test_x.csv', 'w') as outfile:
    for slice_2d in np.array(test_x.items()):
        savetxt(outfile, slice_2d)
with open('train_x.csv', 'w') as outfile:
    for slice_2d in np.array(train_x.items()):
        savetxt(outfile, slice_2d)
"""
#df = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
#savetxt('test_x.csv', np.array(test_x.items()), fmt='%f,%f,%i,%f,%f')
#savetxt('train_x.csv', np.array(train_x.items()), fmt='%f,%f,%i,%f,%f')
#print(f'Processed {line_count} lines.')