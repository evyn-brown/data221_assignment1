# given a list of pairs (x,y), compute x^y for each pair on list, computed and stored in a new list

# define function to take input of a list and compute the exponents of pairs
def exponentiationOfList(pairs=[]):
    # define function to compute exponentiation for all positive integers
    def exponentiation(x, y):
        # return none is exponent is negative
        if y < 0:
            return None
        # return computation when exponent is positive
        else:
            return x ** y

    # create new list for computed exponentiation
    exponentsComputed = []

    # iterate through each pair in list
    for pair in pairs:
        # set x to first number in pair
        x = pair[0]
        # set y to second number in pair
        y = pair[1]
        # set result to calling of exponentiation finction
        result = exponentiation(x, y)
        # if the result is not none, add computation to list for computed values
        if result != None:
            exponentsComputed.append(result)

    # print the calculations to terminal
    print(exponentsComputed)

#example input/output
exponentiationOfList(pairs=[[1, 2], [3, -1], [5, 6], [7, 8]])
