import numpy as np

######################### Random values in a given shape.
a=np.random.rand(2,3)
print(a)
# [[ 0.7524278   0.21176809  0.73990734]
#  [ 0.28341776  0.11559792  0.15859365]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.ndarray'>
print(type(a[0][0]))
# <type 'numpy.float64'>

####################### Return a sample from the standard normal distribution
a=np.random.randn(5)
print(a)
# [ 1.0000366   0.0906066  -0.05027158 -0.14745128  1.35046138]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>

#######################Return a sample from the standard normal distribution
a=np.random.randn(5,4)
print(a)
# [[ 1.48864593 -0.75508993  1.57585151 -0.02507804]
#  [-1.11795072  0.16357727  0.76753395  0.02291213]
#  [-1.39439533  0.66704929 -0.01020978  0.12887067]
#  [-0.19386682  0.70650588  0.71049381 -0.40089744]
#  [-0.6845585   0.35872981  0.18581329 -0.51889034]]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>
print(type(a[0][0]))
# <type 'numpy.float64'>

###############Return random integers from low (inclusive) to high (exclusive).
a=np.random.randint(2,14,size=5)
print(a)
# [12  9  7  3  9]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.int64'>

###############Return random floats in the half-open interval [0.0, 1.0).
a=np.random.random_sample(5)
print(a)
# [-0.20534297  0.4333096   0.94111548 -0.61324519  0.8843922 ]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>


###############Draw samples from a binomial distribution.
n,p=10,0.5 # number of trials, probability of each trial
a=np.random.binomial(n,p,100)
print(a)
# [5 2 5 6 5 3 6 8 5 7 3 4 8 4 9 5 5 6 3 5 7 6 6 2 6 5 6 6 5 3 6 5 6 6 4 6 2
#  7 5 6 7 6 3 3 3 8 8 3 2 5 7 6 4 2 5 7 6 4 5 6 5 5 5 7 4 2 8 3 5 3 6 5 4 4
#  3 3 5 7 7 4 4 6 4 5 6 7 5 5 6 6 4 7 4 4 3 2 6 6 7 3]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.int64'>

############### Draw samples from a uniform distribution.
a=np.random.uniform(5,15,(3,))
print(a)
# [ 13.81416285   5.82087405  13.24553233]
print(type(a))
# <type 'numpy.ndarray'>
print(type(a[0]))
# <type 'numpy.float64'>