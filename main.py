import csv
import pandas as pd
from pandas import DataFrame


# df1 = pd.read_csv('Relocated_Vehicles.csv')
# df1 = pd.read_csv('Towed_Vehicles.csv')
#
def square(list):
    newList = []
    for i in list:
        newList.append(i ** 2)
    return newList

def multiplyList(list1,list2):
    newlist = [a*b for a,b in zip(list1,list2)]
    return newlist


def addElementsInList(list):
    newlist = []
    for row in list:
        newlist = sum(list)
    return newlist


def Ahat(listX, listY):
    import math
    sigmaX = addElementsInList(listX)
    sigmaY = addElementsInList(listY)
    sigmaXY = sum((multiplyList(listX,listY)))
    n = len(list1) # might want to make a f(x) call here
    sigmaXThenSquared = math.pow(sigmaX,2)
    sigmaXSquared = sum(square(listX))
    numerator = (sigmaX*sigmaY) -  (n*sigmaXY)
    # print(numerator)
    dummy = n*sigmaXY
    denominator = (sigmaXThenSquared - dummy)
    slope = numerator/denominator
    return slope

def bHat(listX, listY):
    import math
    sigmaX = addElementsInList(listX)
    sigmaY = addElementsInList(listY)
    sigmaXY = sum((multiplyList(listX,listY)))
    sigmaXSquared = sum(square(listX))
    n=len(listX)
    numerator = (sigmaX*sigmaXY) - (sigmaY*sigmaXSquared)
    sigmaXThenSquared = math.pow(sigmaX,2)
    dummy = n*sigmaXSquared
    denominator =  (sigmaXThenSquared) - dummy
    yIntercept = numerator/denominator
    return yIntercept

def standardDeviationX(listX):
    import math
    sigmaXSquared = sum(square(listX))
    n=len(listX)
    sigmaX = addElementsInList(listX)
    sigmaXThenSquared = math.pow(sigmaX,2)
    numerator = (sigmaXSquared) - (1/n * sigmaXThenSquared)
    final = numerator/(n-1)
    print(final)






list1 = [-1,1,2,4,6,7]
list2 = [-1,2,3,3,5,8]

standardDeviationX(list1)

# print bHat(list1,list2)

# listXSquared = square(list1)
# listYSquared = square(list2)
# listXtimeY = multiplyList(list1,list2)
# sumofListX = addElementsInList(list1)
# sumofListY = addElementsInList(list2)
# sumofListXSquared = addElementsInList(listXSquared)
# sumofListYSquared = addElementsInList(listYSquared)
# sumofListXtimeY = addElementsInList(listXtimeY)
# n = len(list1)
# print slope()








#
# f = open('LoanStats3d.csv', 'rb')
# reader = csv.reader(f)
#
# for row in reader:
#     print(row)
# f.close()
#

