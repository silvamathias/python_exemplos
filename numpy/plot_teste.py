import matplotlib.pyplot as plt
import quandl
#petr4 = quandl.get('BCB/433').reset_index(drop=True)
#print(petr4)
dol=quandl.get('BCB/433', start_date = '2012-01-01', end_date = '2018-12-31').reset_index(drop=True)
#print(dol)
plt.plot(dol)
plt.show();
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()
