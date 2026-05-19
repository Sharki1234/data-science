import numpy as np
# # nums = [1,2,3,4,5]
# # array = np.array([[1,7],[3,6],[8,4]])

# # print(array.ndim)#dimension
# # print(array.shape)#how many in each column then row (3,2)
# # #|1 2|
# # #|2 4|
# # #|5 6|-2 dimentional tensor(visualisation)


# # random_array = np.arange(2,10,2)# makes array from 0 to 9 skips 2 so returns[0,2,4,6,8]
# # print(random_array)

# # reshaped_array = array.reshape(2,3)
# # print(reshaped_array)

# # shuffled = np.random.permutation(random_array)
# # print(shuffled)

# # sorted_array = np.sort(array)[::-1]
# # print(sorted_array)

# #array splicing
# # linear_array = np.array([1,2,3,4,5,6,7,8,9,0])
# # print(linear_array[::3])
# # print(linear_array[:2])
# # print(linear_array[4:7])

# # multi = np.array([[1,2,3],[4,5,6],[7,8,9]])
# # print(multi[0:2,0:1])

# # nums = np.array([np.arange(1,8),np.arange(1,8),np.arange(1,8),np.arange(1,8),np.arange(1,8),np.arange(1,8),np.arange(1,8)])
# # print(nums[2:5,2:5])

# #maths
# array = np.array([10,20,30])
# print(array*2)#[20 40 60]

# lis = [10,20,30]
# print(lis*2)#[10, 20, 30, 10, 20, 30]

# nums = np.array([1,5,3,7,2,8,4,5,6,0,2])
# even_nums= nums[nums%2==0]#check for even numbers acta as if statement
# print(even_nums)#[2 8 4 6 0 2]

# bool_nums=nums[nums == 5]#puts in list if value is a 5
# print(bool_nums)#[5 5]

# print(nums[[2,4,6]])#[3 2 4] prints this index

# sample = np.arange(1,5)
# sample+=1
# print(sample)#all values in sample increased by one

# sample1 = np.arange(1,5)
# sample2 = np.arange(1,5)
# print(sample1+sample2)#[2 4 6 8] adds the arrays

# matrixA= np.random.permutation(np.arange(1,37)).reshape(6,6)
# matrixB= np.random.permutation(np.arange(1,37)).reshape(6,6)
# print(matrixA+matrixB)#Output:
# #[[47 30 46 44 24 28]
# #  [40 13 46 45 48 14]
# #  [31 68 24 36 31 44]
# #  [22 30 15 51 43 55]
# #  [38 33 54 54 43 27]
# #  [49 44 35 39 31 10]]

# allowance = np.array([10, 15, 10, 20])
# chores = np.array([5, 0, 15, 5])
# total = allowance+chores
# magic_total = total*3
# print(magic_total)

hw1 = np.arange(1,16)
hw2 = hw1[hw1<8]

hw3 = hw1[hw1>=10]
hw4 = hw1[hw1%2 == 1]
print(hw1)
print(hw2)
print(hw3)
print(hw4)
