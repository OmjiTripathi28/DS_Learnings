"""Q1 — Basic Array Creation

Create a NumPy array: [5, 10, 15, 20]"""

import numpy as np
b = np.array([5, 10, 15, 20])
print(b)



"""Q2 — Type Understanding

Create: [1, 2.5, 3]

👉 Then print its dtype 👉 Explain WHY it became that type"""

c = np.array([1,2.5,3])
print(c)
print(c.dtype)


"""Q3 — Dimensions Check

Create:

[[1, 2, 3], [4, 5, 6]]

Print: shape ndim size"""

d = np.array([[1, 2, 3], [4, 5, 6]])
print(d.shape,d.ndim,d.size)



"""Q4 — 3D Thinking (IMPORTANT 🔥)
Create a 3D array like:
[[[1,2],[3,4]], [[5,6],[7,8]]]
👉 Then print: shape ndim"""

e = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(e.shape,e.ndim,e.size)


"""Q7 — Manual Thinking
Create a 2D array with: 3 rows 2 columns
👉 Fill with any numbers"""

d = np.array([[1, 2], [4, 5], [7, 8]])
print(d.shape)


"""Q8 — Data Type Control
Create an array: [1, 2, 3]
👉 Force its datatype to float"""
f = np.array([[1, 2, 3]])
print(f.astype(float))

#CHAPTER 2 LEVEL 1: ARRAY CREATION (REAL NUMPY STARTS)
"""Q1

Create a 3×3 matrix of zeros (int type)

Q2

Create an array from 1 to 15 with step 2

Q3

Create 5 equally spaced numbers between 10 and 50

Q4

Create a 4×4 identity matrix

Q5 🔥

Create a 2×3 matrix with random integers between 10 and 50"""