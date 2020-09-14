import csv
test_x = {}
test_x_count = 0
train_x = {}
train_x_count = 0
with open('AUD_JPY_price.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if line_count < 9000:
            test_x[test_x_count] = [row["buy price"],row["sell price"],row["volume"],row["close"],row["open"]]
            test_x_count += 1
        else:
            train_x[train_x_count] = [row["buy price"],row["sell price"],row["volume"],row["close"],row["open"]]
            train_x_count += 1
        #print(f'\t{row["bar#"]} : {row["buy price"]}, {row["sell price"]}, {row["volume"]}, {row["close"]}, {row["open"]}')
        line_count += 1
    print(f'Processed {line_count} lines.')