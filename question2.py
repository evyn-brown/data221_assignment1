# receive a list of strings and return a dictionary such that:
# Each key is a string from the list
# Each value is another dictionary containing
# The length of the string
# Whether the length is even or odd

# define function taking a list as input
def stringToDictionary(userList=[]):
    # create new empty dictionary
    dictionary = {}

    # for loop iterates through each string in the given list
    for i in range(0, len(userList)):
        # get string at given index
        string = userList[i]
        # compute length of string
        stringLength = len(string)

        # if string length is even (zero remainder when divided by 2):
        if stringLength % 2 == 0:
            # set parity to even
            evenLength = "even"
        # else (remainder when divided by zero)
        else:
            # set parity to odd
            evenLength = "odd"

        # create new variable to add to dictionary
        # set key to string
        # set value to another string containing keys and value for: length, parity
        newItem = {string: {"length": stringLength, "parity": evenLength}}
        # add new item to dictionary
        dictionary.update(newItem)

    # function returns dictionary
    return print(dictionary)


#example input/output:
stringToDictionary(["data", "science"])