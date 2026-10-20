# Array indexing (part2)

import numpy as np

arr= np.array([[['A','B','C'], ['E','F','G'],['H','I','J']],
              [['K','L','M'],['N','O','P'],['Q','R','S']],
              [['T' , 'U','V'], ['W','X','Y'],['D','Z','C']]])

word= arr[0,0,0] + arr[0,2,1] + arr[2,2,1]
print(word)


#Slicing

arr = np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12],
               [13,14,15,16]])

#array[start:end:step]
print(arr[-1])
print(arr[3])
print(arr[0:3])
print(arr[0:0:1])
print(arr[::3])
print(arr[2:1:4])
print(arr[:1:-3])

# For the column selection
print(arr[:,0]) #for row we must put: here [row:row ,column:column]
print(arr[:, 1::2])
