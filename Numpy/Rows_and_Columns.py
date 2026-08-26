import numpy as np
x = [[1,2,3],[4,5,6],[7,1,0]]
arr = np.array(x)
print(arr)
arr_new = arr.sum(axis=0)
print(arr_new)
arr_new1 = arr.sum(axis=1)
print(arr_new1) 
for item in arr.flat:
    print(item)