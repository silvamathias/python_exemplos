import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
import matplotlib.pyplot as plt

s = 'ExpNumpy.xlsx'
#wb=workbook ()
wb2=load_workbook(s)
ws=wb2.get_sheet_by_name('Sheet1')
data = ws.values
cols = next(data)[0:]
data = list(data)
#idx = [r[0] for r in data]
#data = (islice(r, 1, None) for r in data)
df = pd.DataFrame(data, columns=cols)
print(df)
p=df.serie1
print('---descricoes--------------------------------')
print(df.describe())
print('---correlacao--------------------------------')
corr = df.corr()
print(corr)

mcorr=np.array(corr,dtype=np.float64)
m2=np.array([[1],[2],[4],[3]],dtype=np.float64)
print('--------mcorr+m2---------------------------')
print(mcorr+m2)
print('--------np.add(mcorr,m2)---------------------------')
print(np.add(mcorr,m2))
print('--------(mcorr-m2)---------------------------')
print(mcorr-m2)
print('--------np.subtract(mcorr,m2)---------------------------')
print(np.subtract(mcorr,m2))
print('--------mcorr*m2---------------------------')
print(mcorr*m2)
print('--------np.multiply(mcorr,m2)---------------------------')
print(np.multiply(mcorr,m2))
print('--------np.dot---------------------------')
print(np.dot(mcorr,m2))
print('-----------------------------------')
print(m2)
print('-----------------------------------')
print(np.linalg.inv(mcorr))
#corr.style.background_gradient()

"""
k={
('media',np.average(p)),
('moda',np.median(p)),
('mediana',np.mean(p))
}
print(k)
print(k.add('media'))

plt.plot(df)
plt.show()
"""

