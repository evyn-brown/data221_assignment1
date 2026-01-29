#example input
#seconds=int(input("Enter a number of seconds past midnight: "))

# function to receive seconds as input and convert it to the designated time of day
def secondToTime(seconds=0):
    # return error message if user enters negative seconds value
    if seconds < 0:
        return "seconds must be a positive value, exiting program"
        # integer division to get hours (1h=3600s)

    #return error if user inputs too many seconds
    elif seconds>86400:
        return "Input seconds exceed number of seconds in a day, exiting program"

    hour = seconds // 3600
    # remainder of second/3600h to get remaining seconds
    remainingSeconds = seconds % 3600
    # integer division to get remaining seconds as minutes
    minutes = remainingSeconds // 60
    # remainder division to get remaining seconds
    seconds = remainingSeconds % 60

    # if statement - hour less than 12 is in AM
    if hour in range(0, 12):
        # set meridiem to AM
        meridiem = "AM"
        # if hour is 0, revert to 12am
        if hour == 0:
            hour = 12

    # hour greater than 12 is in PM
    elif hour >= 12:
        # compute PM hour in 12h clock format
        hour = hour - 12
        # set meridiem to PM
        meridiem = "PM"

    # format return statement
    formatTime = f"{hour} {minutes} {seconds} {meridiem}"

    # return formated time
    return formatTime

#example input/output
print(secondToTime(100))
