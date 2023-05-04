# Exercício contido em: https://www.youtube.com/watch?v=e2lHyMl1IYY
# Objetivo: Minimizar 3x¹ + 5x² (OBS: Sinal inverte no código)
# Sujeito a:
            #  x¹       <=  4
            #       2x² <= 12
            # 3x¹ + 2x² <= 18
            # x¹ >= 0
            # x² >= 0
import numpy as np
from scipy.optimize import linprog

A = np.array([[1,0], [0,2],[3,2]])
b = np.array([4,12,18])
c = np.array([-3,-5])

res = linprog(c, A_ub=A, b_ub=b, bounds=[[0, None],[0, None]], method='revised simplex')
#res = linprog(c, A_eb=A, b_eb=b,bounds=(0, None))
print(A)
print(b)
print(c)

print('Optimal value:', res.fun, '\nX:', res.x)
print('\n---------------------------')
print(res)
