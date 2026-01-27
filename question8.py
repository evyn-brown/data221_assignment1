#import package
import pandas as pd

#set Data
data = {
    "A":[1,2,2,1],
    "B":[3.1,4.2,1.5,6.3],
    "C":[800,150, 400,210]
}
#create data frame from existing data
dataFrame=pd.DataFrame(data)

#add new column, column D which is the sum of values in the rows of column A and B
dataFrame["D"]=dataFrame["A"]*(dataFrame["C"]+dataFrame["B"])
print(dataFrame)
