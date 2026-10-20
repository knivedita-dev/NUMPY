import numpy as  np

'''Filtering = rafers to the process of selecting elements 
from an array that match a given comdition'''

ages = np.array([[21,34,23,23,19,26,35],
                 [34,45,39,48,51,17,21]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 30)]
olderadults = ages[(ages>30) & (ages <55)]

print(teenagers)
print(adults)
print(olderadults)

even = ages[ages % 2 ==0 ]      #boolean masking in numpy
print(even)
odd = ages[ages % 2 ==1] 
print(odd)