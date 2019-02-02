import numpy as np
from matplotlib import pyplot as plt

n = 50
x = np.arange(1,n+1,1)
y = a=np.random.uniform(5,15,(n,))

print('x',x)
print('y',y)

plt.scatter(x,y,s=None, marker='o',color='g',edgecolors='g',alpha=0.9,label="Jagur")
plt.show()