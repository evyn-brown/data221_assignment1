import math

# receive input values from user of raddi of 2 circles
raddiCircle1 = float(input("Enter the radius of the first circle: "))
raddiCircle2 = float(input("Enter the radius of the second circle: "))


# create function to return percentage of circle that could be covered by smaller circle
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    # return non if user inputs negative raddi
    if radiusOfCircle1 < 0 or radiusOfCircle2 < 0:
        # display message to user
        print("Radius of Circle must be positive, cannot compute areas of circles :(")
        return None

    # message to communicate that user has input propper values
    else:
        print("Both circles have positive radiis, now computing calculations...")

    # get exact value for pi
    pi = math.pi

    # compute area of both circles using area formula
    areaCircle1 = pi * (radiusOfCircle1 ** 2)
    areaCircle2 = pi * (radiusOfCircle2 ** 2)

    # case1: circle1>circle2
    if areaCircle1 > areaCircle2:
        # compute percentage larger
        percentageLarger = (areaCircle2) / (areaCircle1) * 100
    # case 2  circle1<circle2
    else:
        # compute percentage larger
        percentageLarger = (areaCircle1) / (areaCircle2) * 100

    # return result to user
    return percentageLarger


# call function
result = circleAreaCoverage(raddiCircle1, raddiCircle2)

# if result is not None, display final message
if result != None:
    print("The percentage of the larger circle’s area that can be covered by the smaller circle is: ", result, "%")
