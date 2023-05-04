import numpy as np
from scipy.optimize import linprog

A = np.array([[0.4, 0.5], [0, 0.2], [0.6, 0.3], [1, 0], [0, 1]])
b = np.array([20, 5, 21, 0, 0])
c = np.array([-40, -30])

res = linprog(c, A_ub=A, b_ub=b,bounds=(None, None))
print('Optimal value:', res.fun, '\nX:', res.x)
#res = linprog(c, A_ub=A
