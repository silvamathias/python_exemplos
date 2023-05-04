"""
disponível em:
http://cs231n.github.io/python-numpy-tutorial/#numpy
acessado em: 2019/02/14
"""
import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print('-----------------------------------')
print(np.dot(v, w))
print('-----------------------------------')
# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print('-----------------------------------')
print(np.dot(x, v))
print('-----------------------------------')

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print('-----------------------------------')
print(np.dot(x, y))
