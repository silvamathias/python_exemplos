import numpy as np
from scipy.optimize import linprog

A = np.array([[-2,-1], [-1,-2]])
b = np.array([-100, -100])
c = np.array([20,30])

res = linprog(c, A_ub=A, b_ub=b, bounds=[[ 0, None],[ 0, None]] , method = 'revised simplex') 
#res = linprog(c, A_eb=A, b_eb=b,bounds=(0, None))
print(A)
print(b)
print(c)
print('Optimal value:', res.fun, '\nX:', res.x)
print('\n---------------------------')
print(res)
