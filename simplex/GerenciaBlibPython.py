import matplotlib.pyplot as plt
import quandl
petr4 = quandl.get('BCB/433')
print(petr4)
#dol=quandl.get('bcb/1', start_date = '2014-01-01', end_date = '2017-12-21')
#print(dol)
#t_index(drop=True)
#plt.plot(dol)
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()
a=[40,0]
b=[0,0]
#plt.plot(b,a)
#plt.show()
plt.Line2D(b,a)
plt.show()
