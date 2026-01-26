#create a loop to consecutively multiply integers until first instance where
#product is greater than threshold value

#initialize variables: threshold value, product of consecutive integers, current number as 1
thresholdValue=100
product=1
currentNumber=1

#while loop to compute product until product is greater than threshold value
while product<thresholdValue:
    #multiply current number by its following consecutive number
    product=currentNumber*(currentNumber+1)
    #increment current number
    currentNumber+=1

#print the first integer where the product becomes greater than threshold value
print("The integer where the product becomes greater than threshold value is: ", currentNumber)

#print product of consecutive numbers greater than threshold value
print("The product of two consecutive integers which is greater than the threshold is : ", product)