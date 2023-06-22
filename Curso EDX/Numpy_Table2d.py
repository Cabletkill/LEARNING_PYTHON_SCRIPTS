import numpy as np
a=[[11,12,13],[21,22,23],[31,32,33]]
A=np.array(a)

print(A)
print(A.ndim)
print(A.shape)

print(A[1][2])

x=np.array([[1,0],[0,1]])
y=np.array([[2,1],[1,2]])
print(x*y%3)