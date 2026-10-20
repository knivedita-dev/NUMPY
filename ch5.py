# Broadcasting

'''Broadcasting allows Numpy to perform the operations on arrays
with different shapes by virtually expanding dimensions
so they match the larger array shape .

the dimension have the same size.

0R
One of the dimension has size of 1'''


import numpy as np 

arr1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(arr1.shape)
print(arr2.shape)
# output (raw :column) in arr1 as bs ek set hai
#   arr2 mein har ek element apne mein ek set hai,
# bs likne ke lie [[]] yesa h but its mean [ []  
#                                            []
 #                                           []     ]

print(arr1 * arr2) #table to 10