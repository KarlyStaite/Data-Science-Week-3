import numpy as np
array = np.arange(1,11,1)
for i in range(len(array)):
    if(not i%2==1):
            array[i]=-1

print(np.reshape(array,[2,5]))
