import random
import csv
import os


## CONFIGURATION
currentDirectory = os.getcwd()
os.mkdir("{0}\\batchDataOutput".format(currentDirectory))



### DATE GENERATOR
### --------------
### Generates list of date ranges for the months Jan --> June

### STORE LIST
### ------------
### Reading the storedata.csv to get store information

stores=[]
with open('{0}\\storedata.csv'.format(currentDirectory)) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    products = []
    for row in csv_reader:
        stores.append(row)
stores = stores[1:]

print(stores)

monthLengths = [31, 28, 31, 30, 31, 30, 31, 31]
startDates = [1546300800, 1548979200, 1551398400, 1554076800, 1556668800, 1559347200, 1561939200, 1564617600]
monthNames = ["jan", "feb", "mar", "april", "may", "jun", "jul", "aug"]
day = 86400
dateRanges = []
for idx, length in enumerate(monthLengths):
    startDate = startDates[idx]
    dateRanges.append(list(range(startDate, startDate + (day * (length)), day)))


### PRODUCT LIST
### ------------
### Reading the GROCERY_DATA.csv to generate a Python List of products based off the CSV

with open('{0}\\GROCERY_DATA.csv'.format(currentDirectory)) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    products = []
    for row in csv_reader:
        products.append(row)

### PRODUCTS
### --------
### List of the products to be used for generating sales
products = products[1:]


letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
transactionIDStart = 5123
# for each store in storeids
storeList = []
print("Beginning Store Data Generation")
for idx, store in enumerate(stores):
    targetStore = store[0]
    print(targetStore)
    storeTransactions = []
    # for month in each daterange
    for month in dateRanges:
        transactionsInMonth = []
        for day in month:
            numOfTransactions = random.randint(100, 200)
            for transaction in range(0, numOfTransactions):
                numOfProductsPerTransaction = random.randint(1,100)
                transactionLetter = letters[random.randint(0,25)]
                transactionIDnum = str(transactionIDStart)
                for product in range(0, numOfProductsPerTransaction):
                    prodID = products[random.randint(0, 298)]
                    row = [str(targetStore) + "-" + transactionIDnum + "-" + transactionLetter,day,int(prodID[0]),prodID[3],prodID[-1],prodID[4],prodID[5],store[1],store[2]]
                    transactionsInMonth.append(row)
                transactionIDStart+= 1
        storeTransactions.append(transactionsInMonth)
        print("Month of Data Generated for {0} Store".format(store))
    storeList.append(storeTransactions)

import pandas as pd

for idx, storeF in enumerate(storeList):
    for idxj, monthj in enumerate(storeF):
        df = pd.DataFrame(monthj, columns=["transactionID", "transactionDate", "productID", "category", "price", "brand", "productName", "zipcode", "state"])
        df.to_csv("{2}\\batchDataOutput\\{0}_{1}.csv".format(stores[idx][0], monthNames[idxj], currentDirectory), index=False)
    
    


                