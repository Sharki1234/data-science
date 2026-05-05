import numpy as np
nums = [1,2,3,4,5]
array = np.array([[1,7],[3,6],[8,4]])

print(array.ndim)#dimension
print(array.shape)#how many in each column then row (3,2)
#|1 2|
#|2 4|
#|5 6|-2 dimentional tensor(visualisation)


random_array = np.arange(2,10,2)# makes array from 0 to 9 skips 2 so returns[0,2,4,6,8]
print(random_array)

reshaped_array = array.reshape(2,3)
print(reshaped_array)

shuffled = np.random.permutation(random_array)
print(shuffled)

sorted_array = np.sort(array)[::-1]
print(sorted_array)