import numpy as np

#np.where is searching function hai.
# tum condition do aur ye batata hai
# kaun se element uss condition pr fit hote hai

arr = np.array([10,25,3,40,18])
# np.where(arr >=15)
print(arr[np.where(arr >=15)])

