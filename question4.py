# sort list of random numbers (between 0 and 1) in ascending order, given random value X, find instance in list where the number is greater than x

from random import random

# Create list containing 20 random floats between 0 and 1
randomValues = [random() for i in range(20)]

# get random x value
x = random()

# sort list of random values into ascending order
sortedList = sorted(randomValues)

# initialize list for numbers greater than x
valueGreaterThanX = []
# initialize list for index where number is greater than x
indexGreaterThanX = []

# iterate through each item in sorted list
for item in sortedList:
    # if item is greater than x, append to list for items greater than x
    if item > x:
        valueGreaterThanX.append(item)

# iterate through sorted list
for i in range(0, len(sortedList)):
    # append each index of number where it the number is greater than x
    if sortedList[i] > x:
        indexGreaterThanX.append(i)

# assign variable to first index where number is greater than x
firstIndexGreaterThanX = indexGreaterThanX[0]

# print result to user
print("sorted list: ", sortedList)
print("X value: ", x)
print("First index greater than X: ", firstIndexGreaterThanX, " With a value of: ", valueGreaterThanX[0])