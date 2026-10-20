# Aggregate functions = summarize data and typically returns 
# a single value
import numpy as np
arr = np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))    #Standars deviation
print(np.var(arr))   #varition
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr)) #position of min 

#  if you want to add all column and row specifically
print(np.sum(arr, axis=1))      # axis 1 for raw
print(np.sum(arr, axis = 0))   #axis 0 for column

