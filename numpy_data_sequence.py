import numpy as np

a = np.array([1, 2, 3])
print(a)
#[1 2 3]
print(type(a))
#<type 'numpy.ndarray'>
b = np.array([[1, 2], [3, 4]])
print(b)
#[[1 2]
# [3 4]]
#################################################################
c = np.arange(3)
print(c)
# [0 1 2]
print(type(c))
# <type 'numpy.ndarray'>
print(type(c[0]))
# <type 'numpy.int64'>

d = np.arange(3.0)
print(d)
# [ 0.  1.  2.]
print(type(d))
# <type 'numpy.ndarray'>
print(type(d[0]))
# <type 'numpy.float64'>

e = np.arange(5 ,10, 1,dtype=np.float64)
print(e)
# [ 5.  6.  7.  8.  9.]
print(type(e))
# <type 'numpy.ndarray'>
print(type(e[0]))
# <type 'numpy.float64'>

##################################################################
a=np.linspace(2, 13, num=5,dtype=np.float64)
print(a)
# [  2.     4.75   7.5   10.25  13.  ]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>

a=np.logspace(1, 2, num=5,dtype=np.float64)
print(a)
# [  10.           17.7827941    31.6227766    56.23413252  100.        ]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>


a=np.geomspace(1, 2, num=5,dtype=np.float64)
print(a)
# [ 1.          1.18920712  1.41421356  1.68179283  2.        ]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>