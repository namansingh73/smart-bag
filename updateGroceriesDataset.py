import numpy as np
from numpy.core.fromnumeric import sort
from numpy.core.numeric import NaN
import pandas as pd
from fuzzywuzzy import fuzz
import datetime
import random

df = pd.read_csv("orderHistory.csv")
productList = pd.read_csv("products.csv")
brandList = productList['brand'].values.tolist()
brands = []
for index, order in df.iterrows():
    # print(order['pid'])
    brands.append(brandList[order['pid']])

df['brand'] = brands

df.to_csv("orderHistory.csv", index=False)

# DISCOUNTS
# df = pd.read_csv("products.csv")
# pidList = df['pid'].values.tolist()
# for i in pidList:
#     df.at[i,'product_name']= str(df.at[i,'product_name']).capitalize()
# df.to_csv("products.csv",index=False)
# allData=[]
# for pid in pidList:
#     randomDiscount = random.randint(0,10)
#     currentData = [pid,randomDiscount]
#     allData.append(currentData)
# newDf = pd.DataFrame(data = allData,columns=['pid','discount'])
# newDf.to_csv("discounts.csv",index=False)
# def getPriceWeights(products):
#         productList = products.values.tolist()
#         maxPrice = int(products['price'].max())
#         minPrice = int(products['price'].min())
#         # print(minPrice)
#         # print(maxPrice)
#         priceData=[]
#         for product in productList:
#             price = int(product[2])
#             currentData = float((price-minPrice)/(maxPrice-minPrice))
#             # currentData = 1/(1+math.exp(-currentData))
#             priceData.append(currentData)
#         # print(priceData)
#         return priceData

# df = pd.read_csv("products.csv")
# pidList = df['pid'].values.tolist()
# pnameList = df['product_name'].values.tolist()
# pbrandList = df['brand'].values.tolist()
# randomString = "kwwonhinmacdyk"
# minNameScore = 1000000000
# maxNameScore = 0
# minBrandScore = 100000000
# maxBrandScore = 0
# for pid in pidList:
#     pname = pnameList[pid]
#     pbrand = pbrandList[pid]
#     val = fuzz.ratio(randomString,pname)
#     print(pname, val)
#     maxNameScore = max(maxNameScore,val)
#     minNameScore = min(minBrandScore,val)
#     val2 = fuzz.ratio(randomString,pname)
#     maxBrandScore = max(maxBrandScore,val2)
#     minBrandScore = min(minBrandScore,val2)


# allData = []
# nameData = []
# brandData = []
# priceData = getPriceWeights(df)
# for pid in pidList:
#     pname = pnameList[pid]
#     pbrand = pbrandList[pid]
#     val = fuzz.ratio(randomString,pname)
#     normalizedName = float((val-minNameScore)/(maxNameScore-minNameScore))
#     nameData.append(normalizedName)
#     val2 = fuzz.ratio(randomString,pbrand)
#     normalizedBrand = float((val2-minBrandScore)/(maxBrandScore-minBrandScore))
#     brandData.append(normalizedBrand)

# totalData=[pidList,priceData,nameData,brandData]
# index = ['pid','price','name','brand']
# newData = pd.DataFrame(data=totalData,index=index,columns=pnameList)
# newData = newData.T
# newData.to_csv("correlationData.csv",index=False)


# df = pd.read_csv("Groceries_datasetNewPrice.csv")

# FOR DATE
# for i in range(0,df.shape[0],10):
#     randomMonth = random.randint(0,5) + 4
#     randomDate = random.randint(1,28)
#     for j in range(i,i+10):
#         df.loc[j,'Date']  = datetime.datetime(2021,randomMonth,randomDate).strftime("%d/%m/%Y")
# df.to_csv("Groceries_datasetNewPrice.csv",index=False)

# for i in range(0,df.shape[0],5):
#     randomUid = random.randint(1,2001)
#     for j in range(i,i+5):
#         df.loc[j,'oid'] = int(i/5 + 1)


# print(df)
# df.to_csv("Groceries_datasetNew.csv",index=False)


# map={}
# for i in range(0,df.shape[0]):
#       currentProduct = df.loc[i,'product_name']
#       if currentProduct in map:
#             df.loc[i,'price'] = map[currentProduct]
#       else:
#             randomPrice = random.randint(50,500)
#             df.loc[i,'price'] = randomPrice
#             map[currentProduct] = randomPrice
# print(df)
# df.to_csv("Groceries_datasetNewPrice.csv",index=False)
# n = len(pd.unique(df['uid']))


# set={"tropical","fruit"}
# for i in range(0,df.shape[0]):
#       currentProduct = df.loc[i,'product_name']
#     #   print(currentProduct)
#       data = str(currentProduct).split()
#       for temp in data:
#             set.add(temp)
# for i in range(0,df.shape[0]):
#       currentProduct = df.loc[i,'product_name']
#       if('/' in str(currentProduct)):
#         data = str(currentProduct).split('/')
#         for temp in data:
#                 set.add(temp)
# # print(set)
# print(len(set))

# n = len(pd.unique(df['uid']))
# uids = pd.unique(df['uid'])
# uids = sort(uids)

# browseData = []
# wordsList = list(set)

# try:
#     for uid in uids:
#         numOfRecords = random.randint(5,7)
#         for i in range(numOfRecords):
#             randNum = random.randint(0,len(wordsList)-1)
#             word = wordsList[randNum]
#             randomDate = random.randint(1,20)
#             randomCompleteDate = datetime.datetime(2021,9,randomDate).strftime("%d/%m/%Y")
#             userData = [int(uid),word,randomCompleteDate]
#             browseData.append(userData)
# except:
#     print("error")

# browseDf = pd.DataFrame(browseData, columns = ['uid','search', 'date'])
# browseDf.to_csv("browseHistory.csv",index=False)

# browseHistory = pd.read_csv("browseHistory.csv")
# browseHistory = browseHistory.sort_values(['uid','date'],ascending=False)
# print(browseHistory)
# browseHistory.to_csv("browseHistory.csv",index = False)


# productsDf = df[['pid',"product_name",'price']]
# productsDf = productsDf.drop_duplicates()
# print(productsDf)
# productsDf = productsDf.sort_values("pid")
# productsDf.to_csv("products.csv",index=False)

# print("No.of.unique values :",
#       n)
