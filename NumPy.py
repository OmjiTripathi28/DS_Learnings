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


"""Q9 — Convert Python List l = [10, 20, 30, 40]
Convert it into NumPy array and: check dtype check shape"""