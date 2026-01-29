
# define function that receives a list of numbers and returns dictionary with key as number from list (Ascending order) and value as percent of numbers in list greater than given number
def returnDictionary(numbers=[]):
    # create new empty dictionary
    newDictionary = {}

    # sort given list into ascending order
    sortedList = sorted(numbers)
    # get length of list
    lengthList = len(sortedList)

    # iterate through each item in sorted list
    for item in sortedList:
        # initialize numSmallerThanItem to zero
        numSmallerThanItem = 0

        # check to see if item is larger or equal to each other item in list
        for i in range(0, lengthList):
            if item >= sortedList[i]:
                # increment numSmallerThanItem if statement is true
                numSmallerThanItem += 1

        # compute percentage of smaller values
        percentSmaller = (numSmallerThanItem / lengthList) * 100
        # create new item for dictionary with value as percentage calculated
        newItemDictionary = {item: f"{percentSmaller:.2f}%"}
        # add new item to dictionary
        newDictionary.update(newItemDictionary)

    # return dictionary
    return newDictionary

#example input/output
print([3, 1, 2, 3, 4, 2])
print(returnDictionary(numbers=[3, 1, 2, 3, 4, 2]))
