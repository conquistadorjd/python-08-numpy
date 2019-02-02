################################################################################################
#	name:	numpy_data_random_01.py
#	desc:	Genarate test data having linear relationship
#	date:	2019-02-02
#	Author:	conquistadorjd
################################################################################################
import numpy as np
from matplotlib import pyplot as plt

print('*** Program Started ***')

n = 50
x = np.arange(-n/2,n/2,1,dtype=np.float64)
y = a=np.random.uniform(-15,15,(n,))

print('x',x)
print('y',y)

plt.scatter(x,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Random numbers")
plt.grid(color='black', linestyle='--', linewidth=0.5,markevery=int)
plt.legend(loc=2)
plt.axis('scaled')
plt.show()

plt.savefig('numpy_data_random_01.jpeg')

print('*** Program ended ***')