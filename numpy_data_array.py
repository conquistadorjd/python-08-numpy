import numpy as np

a=np.identity(3,dtype=np.float64)
print(a)
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.ndarray'>
print(type(a[0][0]))
# <type 'numpy.float64'>

a=np.eye(3, 5, k=0,dtype=np.float64)
print(a)
# [[ 1.  0.  0.  0.  0.]
#  [ 0.  1.  0.  0.  0.]
#  [ 0.  0.  1.  0.  0.]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.ndarray'>
print(type(a[0][0]))
# <type 'numpy.float64'>

a=np.ones((3, 5),dtype=np.float64)
print(a)
# [[ 1.  1.  1.  1.  1.]
#  [ 1.  1.  1.  1.  1.]
#  [ 1.  1.  1.  1.  1.]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.ndarray'>
print(type(a[0][0]))
# <type 'numpy.float64'>

a=np.ones_like(np.array([[0,1,0,2,5],[1,2,3,4,4]]),dtype=np.float64)
print(a)
# [[1 1 1 1 1]
#  [1 1 1 1 1]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.ndarray'>
print(type(a[0][0]))
# <type 'numpy.float64'>


a=np.full((3, 5),22,dtype=np.float64)
print(a)
# [[ 22.  22.  22.  22.  22.]
#  [ 22.  22.  22.  22.  22.]
#  [ 22.  22.  22.  22.  22.]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.ndarray'>
print(type(a[0][0]))
# <type 'numpy.float64'>