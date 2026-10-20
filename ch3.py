# Scalar arithmetic

import numpy as np
arr = np.array([1,2,3,4])
print(arr +1 )
print(arr - 2)
print(arr * 3)
print(arr / 4)
print(arr ** 5)  # ** mean ^ power

# Vatorized math funcs
arr= np.array([1.1, 2.2 ,3.3])
print(np.sqrt(arr))
print(np.round(arr))
print(np.pi)

#Excerise
radii = np.array([2,4,8])
print(np.pi *radii ** 2)  #Area = Pi*r^2
print(np.pi *2*radii)      #Circumference


# Element wise arithmetic

arr1 = np.array([1,2,3])
arr2 = np.array([2,4,8])

print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 ** arr2)
