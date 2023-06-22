
import numpy

a=numpy.array([0,1,2,3,4,5,6])
print(a)
print(type(a))
print(a.dtype)

print()
print()

u=[10,0]
v=[5,1+1]
z=[]
for n, m in zip(u,v):
    z.append(m+n)
    print(z)
