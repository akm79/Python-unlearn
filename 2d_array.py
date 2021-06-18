import numpy as np
twod = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
newd = np.insert(twod,4,[7,4,6,8],axis=0)
print(twod)
print(newd)