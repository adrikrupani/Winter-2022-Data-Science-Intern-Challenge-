# This program
from random import seed

import numpy as np
import pandas as pd

# Importing the dataset from a local .csv file
dataset = pd.read_csv('2019 Winter Data Science Intern Challenge Data Set.csv')
amount = dataset.iloc[:, 3:4].values
items = dataset.iloc[:, 4:5].values


# This functions demonstrates how the challenge question calculated the AOV

def ProvidedMetricForAOV(amt):
    total = 0;
    for i in amt:
        total += i;
    return total / len(amt)


# This function calculates the AOV by excluding outliers while still showing the AOV for the outlier groups
def AlternateMethodForAOV(amt):
    # using truncate mean to calculate mean and identify outliers,
    # using a p = 0.05 (5%)
    output = []
    p = 0.05
    a = sorted(amt)
    n = len(a)
    k = p * n
    truncMean = a[int(k):n - int(k)]
    # lower and upper bound variables are the outlier groups excluded from the main AOV calculation
    lowerBound = a[0:int(k)]
    upperBound = a[n - int(k):n]

    total = 0
    upperTotal = 0
    lowerTotal = 0

    for i in truncMean:
        total += i

    for j in range(int(k)):
        upperTotal += upperBound[j]
        lowerTotal += lowerBound[j]

    # Placing all three AOV calculations into an output list
    output.append(total / (n - (2 * k)))
    output.append(upperTotal / int(k))
    output.append(lowerTotal / int(k))

    return output


# Question 2

# Function to Detection Outlier on one-dimensional datasets. (Altered from a stack overflow post)
def find_anomalies(data):
    # define a list to accumlate anomalies
    anomalies = []
    # Set upper and lower limit to 3 standard deviation
    data_std = np.std(data)
    data_mean = np.mean(data)
    anomaly_cut_off = data_std * 3

    lower_limit = data_mean - anomaly_cut_off
    upper_limit = data_mean + anomaly_cut_off
    # Generate outliers
    for outlier in data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies


# Function used to identity and remove the outlier data points for an optimal calculation
# we use both dictionaries together as we are removing both outlier prices and earning.
# The necessity of this is explained in the README file
def RemoveOutliersFromBothDictionaries(shopProd, shopEarn):
    liP = np.array(list(shopProd.values()))
    liE = np.array(list(shopEarn.values()))

    outliersEarn = find_anomalies(liE)
    outliersProd = find_anomalies(liP)

    outlierProdKeys = []
    for o in outliersProd:
        key = (list(shopProd.keys())[list(shopProd.values()).index(o)])
        outlierProdKeys.append(key)

    outliersEarnKeys = []
    for o in outliersEarn:
        key = (list(shopEarn.keys())[list(shopEarn.values()).index(o)])
        outliersEarnKeys.append(key)

    for oKp in outlierProdKeys:
        shopProd = {key: val for key, val in shopProd.items() if key != oKp}
        shopEarn = {key: val for key, val in shopEarn.items() if key != oKp}

    for oKe in outliersEarnKeys:
        shopProd = {key: val for key, val in shopProd.items() if key != oKe}
        shopEarn = {key: val for key, val in shopEarn.items() if key != oKe}

    return shopProd, shopEarn


def FindingVariablePriceRanges(data_csv):
    # Grabbing columns from dataset
    # and sorting the data by the shop ID (in ascending order)
    Shops = data_csv.iloc[:, 1:5].values
    sShops = sorted(Shops, key=lambda x: x[0])

    # Creating two dictionary functions that store product price and total earning
    # Each key is the shop id and the value is the product price (in shopProd - dictionary)
    # Each key is the shop id and the value is the total earnings (in shopEarn - dictionary)
    shopProd = {}
    shopEarn = {}
    shop_id = 1
    cost = 0
    num_item = 0
    for s_id in sShops:
        cost += s_id[2]
        num_item += s_id[3]
        if s_id[0] != shop_id:
            shopEarn[shop_id] = cost
            shopProd[shop_id] = cost / num_item
            cost = 0
            num_item = 0
            shop_id += 1
    shopProd[shop_id] = cost / num_item
    shopEarn[shop_id] = cost

    # Sorting the two dictionaries by their values
    # this way we have the stores order by lowest product prices to highest (in shopProd - dictionary)
    # and we have the shops ordered by lowest to highest earnings for the month (in shopEarn - dictionary)
    shopProd = dict(sorted(shopProd.items(), key=lambda item: item[1]))
    shopEarn = dict(sorted(shopEarn.items(), key=lambda item: item[1]))

    # Removing our outlier data points that disrupt the calculations
    shopProd, shopEarn = RemoveOutliersFromBothDictionaries(shopProd, shopEarn)

    # Here we separate the data into three generic data points
    brackets = 5
    separation = int(len(shopProd) / brackets)
    separationPoint = separation
    # This calculates the remainder and adds it to the offset to the first bracket of prices
    remainder = len(shopProd) - (separationPoint * brackets)
    separationPoint += remainder

    count = 0
    results = {}
    meanEarn = 0
    meanPrice = 0
    for keyIter in shopProd.keys():
        count += 1;
        meanEarn += shopEarn[keyIter]
        meanPrice += shopProd[keyIter]
        if count >= separationPoint:
            results[float(meanPrice / separation)] = float((meanEarn / separation) / (meanPrice / separation))
            separationPoint += separation
            meanEarn = 0
            meanPrice = 0

    return results


print("\n\t\t\t\t\t\t\t\tQuestion 1: Improved AOV: ")
print("Naive Approach for AOV: ", ProvidedMetricForAOV(amount))
AltAOV = AlternateMethodForAOV(amount)
print("Alternate Calculation for AOV\n",
      "\tAOV: \t\t\t\t\t\t", AltAOV[0],
      "\n\tAOV - (Lower Bound Outliers): ", AltAOV[1],
      "\n\tAOV - (Upper Bound Outliers): ", AltAOV[2])

print("\n\t\t\t\t\t\t\tQuestion 2: Alternate metric: ")
print("\nBracket#:\t\t\tPrice of Shoe:\t\t\tEarnings Potential Multiple: ")
c2Result = FindingVariablePriceRanges(dataset)
iter = 0
for i in c2Result:
    iter += 1
    print(iter, ".\t\t\t\t\t", i, "\t\t\t", c2Result[i])
