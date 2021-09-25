import random
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
import time
import datetime


class Recommender:
    def __init__(self):
        self.orderDetails = self.get_orderDetails()
        self.browserHistory = self.get_browserHistory()
        self.products, self.productList, self.numOfProducts = self.get_products()
        self.correlationData = self.get_correlationData()

    # Retrieve the entire orderHistory dataset
    def get_orderDetails(self):
        orderDetails = pd.read_csv("orderHistory.csv")
        return orderDetails

    # Retrieve the entire browseHistory dataset
    def get_browserHistory(self):
        orders = pd.read_csv("browseHistory.csv")
        return orders

    # Retrieve the entire products dataset, and extract some variables used later
    def get_products(self):
        products = pd.read_csv("products.csv")
        productList = products.values.tolist()
        numOfProducts = len(productList)

        return products, productList, numOfProducts

    # Retrieve the already calculated data used for calculation of correlation matrix.
    def get_correlationData(self):
        correlationData = pd.read_csv("correlationData.csv")
        return correlationData

    """
        Formula used for normalizing values between 0 and 1:
            normalized_x = (maxValue - x)/(maxValue - minValue)
        Attributes used: Price of products, Similarity in Name of product, Similarity in Brand of product,
                         Date of previous orders, Brand Preference of user
    """

    # Calculate weights for the "date" attribute, which gives higher weight to products ordered RECENTLY by the specific user.
    def getDateWeights(self, userId):
        orderHistory = self.orderDetails.loc[self.orderDetails['uid'] == userId]
        dateData = np.zeros(self.numOfProducts)
        maxDate = 0
        minDate = 100000000000

        # calculate minimum and maximum date
        for index, order in orderHistory.iterrows():
            currentPid = order['pid']
            orderDate = order['date']
            orderTimestamp = time.mktime(
                datetime.datetime.strptime(orderDate, '%d/%m/%Y').timetuple())
            maxDate = max(maxDate, orderTimestamp)
            minDate = min(minDate, orderTimestamp)

        # normalize values of date of orders according to minimum and maximum
        for index, order in orderHistory.iterrows():
            currentPid = order['pid']
            orderDate = order['date']
            orderTimestamp = time.mktime(
                datetime.datetime.strptime(orderDate, '%d/%m/%Y').timetuple())
            dateData[currentPid] = 0.2 if float((orderTimestamp-minDate)/(
                maxDate-minDate)) == 0 else float((orderTimestamp-minDate)/(maxDate-minDate))
        return dateData

    # Calculate weights for the "userBrandPreference" attribute, which gives a boolean 1 to Brands previously ordered by the user
    # and a boolean 0 to Brands not ordered by the user.
    def getBrandDataWeights(self, userId):
        orderHistory = self.orderDetails.loc[self.orderDetails['uid'] == userId]
        print(orderHistory)
        userBrandData = np.zeros(self.numOfProducts)
        # to avoid repeating computation for already calculated brand
        visited = set()
        pidsBought = orderHistory['pid'].values.tolist()
        for pid in pidsBought:
            brand = self.products['brand'].values.tolist()[pid]
            if brand not in visited:
                visited.add(brand)
                counter = 0
                for product in self.productList:
                    if product[3] == brand:
                        userBrandData[counter] = 1
                    counter = counter+1
        return userBrandData

    # Function made for testing recommendations of specific products, by prodcutId.
    def getSingleProductRecommendation(self, productId):
        productCorr = self.correlationMatrix[productId]
        newArray = []
        for i in range(0, len(productCorr)):
            newArray.append([productCorr[i], i])
        newArray = sorted(newArray, reverse=True)

        for i in range(0, 10):
            print(productCorr[newArray[i][1]],
                  self.productList[newArray[i][1]])

    """
    Main function being called for recommendations of a specific user. 
    This function takes the user's browse history and finds products related to his recent browse history.
    After these products are retrieved, some random products are sent to the user as recommendations.

    """

    def getProductRecommendation(self, userId):
        correlationMatrix = self.getCorrelationMatrix(userId)
        searchQueries = self.browserHistory.loc[self.browserHistory['uid']
                                                == userId]['search'].values.tolist()
        print(searchQueries)
        productsSimilarToBrowsed = []
        for item in searchQueries:
            for product in self.productList:
                pname = product[1]
                pid = product[0]
                val = fuzz.token_set_ratio(item, pname)
                if val > 75:
                    productsSimilarToBrowsed.append(pid)

        # This part is just adding products according to correlation matrix. Rest of the code is just to avoid repeating entries.
        entireProductListIndex = set()
        for productId in productsSimilarToBrowsed:
            productCorr = correlationMatrix[productId]
            newArray = []
            for i in range(0, len(productCorr)):
                newArray.append([productCorr[i], i])
            newArray = sorted(newArray, reverse=True)

            for i in range(1, 3):  # taking only top product after 1. for now
                entireProductListIndex.add(newArray[i][1])
        entireProductList = []
        for index in entireProductListIndex:
            entireProductList.append(self.productList[index])

        finalProductListIndex = set()
        for i in range(0, min(len(entireProductList), 10)):
            randNum = random.randint(0, len(entireProductList)-1)
            finalProductListIndex.add(randNum)

        print(finalProductListIndex)
        finalProductList = []
        for num in finalProductListIndex:
            finalProductList.append(entireProductList[num])

        for product in finalProductList:
            print(product)
        return finalProductList

    def getCorrelationMatrix(self, userId):

        # Get attribute values ( all normalized between 0 and 1 )
        priceData = self.correlationData['price'].values.tolist()
        dateData = self.getDateWeights(userId)
        nameData = self.correlationData['name'].values.tolist()
        brandData = self.correlationData['brand'].values.tolist()
        userBrandData = self.getBrandDataWeights(userId)

        totalData = [priceData, dateData, nameData, brandData, userBrandData]
        index = ['price', 'date', 'name', 'brand', 'userBrandPreference']

        productXAttributes = pd.DataFrame(
            data=totalData, index=index, columns=self.products['product_name'].values.tolist())

        productXAttributes = productXAttributes.T
        productXAttributes = productXAttributes.astype(float)
        productXAttributes = productXAttributes.dropna()
        productXAttributes.to_csv("TemporaryMatrix.csv", index=False)
        print(productXAttributes)
        print(np.corrcoef(productXAttributes))

        corrcoef = np.corrcoef(productXAttributes)
        return corrcoef

    def getUserOrderHistory(self, userId):
        orderHistory = self.orderDetails.loc[self.orderDetails['uid'] == userId].values.tolist(
        )
        return orderHistory

    def getUserBrowseHistory(self, userId):
        browseHistory = self.browserHistory.loc[self.browserHistory['uid'] == userId].values.tolist(
        )
        return browseHistory

# Enter user ID for testing
# r = Recommender(8)
# r.getProductRecommendation(8)


# Add after index =[] wali line to add dummy random variables
 # for i in range(1,4):
        #     dummyData = []
        #     for product in self.products.values:
        #         dummyData.append(random.random())
        #     totalData.append(dummyData)
        #     index.append('dummy' + str(i))
