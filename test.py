import numpy as np

a = np.array([[1,2,3],
 [2,5,4]])
value = 3

indices = np.where(a[:,0] == value)
print(indices[0][0])
