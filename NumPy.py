# Q1
# Create a null vector of size 10 but the fifth value should be 1.
import numpy as np
a = np.zeros(10)
a[4] = 1
print(a)

# Q2
# Ask user to input two numbers a, b.
# Generate a random array of shape (a, b) and print:
# 1. The array
# 2. The average of the array
import random
a = int(input("enter no. a = "))
b = int(input("enter no. b = "))
array = np.random.random([a,b])
print(array)

# Q3
# Write a function to create a 2D array with 1 on the border and 0 inside.
# Take shape (a, b) as input.
# Example:
# [[1,1,1,1],
#  [1,0,0,1],
#  [1,0,0,1],
#  [1,1,1,1]]
def array():
   a = int(input("enter a number a = "))
   b = int(input("enter a number b = "))
   array = np.zeros(a*b).reshape(a,b)
   array[0,:] = 1
   array[:,0] = 1
   array[a-1, :] = 1
   array[:,b-1] = 1
   print(array)

  
array()

# Q4
# Create a vector of size 10 with values ranging from 0 to 1 (excluded).
a = np.arange(0,1,0.1)
print(a)

# Q5
# Can you create an identity matrix of shape (3,4)?
# If yes, write the code.
"""NO, AN IDENTITY MATRIX OF SHAPE (3,4) CANNOT BE MADE"""

# Q6
# Create a 5x5 matrix with row values ranging from 0 to 4.
b = np.arange(0,5).reshape(5,5)
print(b)

# Q7
# Generate a random integer array (1 to 100) of shape (10,2) representing coordinates.
# Given point:
# point = np.array([2,3])
# Find distance of each point from this point.
# Output should be integer type.


# Q8
# Given an array of shape (6,7,8),
# find index (x, y, z) of the 100th element.


# Q9
# Input: space separated numbers
# Output: reversed NumPy array with float type


# Q10
# Count the number of elements in a numpy array.


# Q11
# Write a function to calculate Softmax of a 1D numpy array.
# Raise error if input is not 1D numpy array.


# Q12
# Write a function that accepts multiple numpy arrays
# and vertically stacks them.
# Raise error if input is not numpy arrays.


# Q13
# Write a function "date_array" that:
# - Takes two date strings (format: YYYY-MM-DD)
# - Returns numpy array of all dates between them (inclusive)
# - Assume same year
# - Raise error if inputs are not strings


# Q14
# Subtract the mean of each row from a matrix.


# Q15
# Swap column 1 with column 2 in a numpy array.


# Q16
# Replace all odd elements in array with -1.


# Q17
# Given two arrays of same shape, create array of max values.
# Example:
# a = [6,3,1,5,8]
# b = [3,2,1,7,2]
# Output: [6,3,1,7,8]


# Q18
# Given:
# arr1 = np.random.randint(1, 10000, size=40).reshape(8,5)
# 1. Fetch every alternate column
# 2. Normalize array using:
#    (X - Xmin) / (Xmax - Xmin)


# Q19
# Write a function:
# Input:
#   arr -> 1D numpy array
#   n -> integer (n <= len(arr))
# Output:
#   nth largest element
# Example:
# arr = [12,34,40,7,1,0], n=3 → output = 12


# Q20
# Create pattern using numpy only:
# Input:
# a = np.array([1,2,3])
# Output:
# [1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3]