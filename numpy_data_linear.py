################################################################################################
#	name:	numpy_data_linear.py
#	desc:	Genarate test data having linear relationship
#	date:	2019-02-02
#	Author:	conquistadorjd
################################################################################################
import numpy as np
from matplotlib import pyplot as plt

print('*** Program Started ***')

n = 50
x = np.arange(-n/2,n/2,1,dtype=np.float64)

m = np.random.uniform(0.3,0.5,(n,))
b = np.random.uniform(5,10,(n,))

y = x*m +b 
print('x',x, type(x[0]))
print('y',y, type(y[0]))

plt.scatter(x,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Linear Relation")
plt.grid(color='black', linestyle='--', linewidth=0.5,markevery=int)
plt.legend(loc=2)

plt.show()

plt.savefig('scarrerplot-01.png')

print('*** Program ended ***')