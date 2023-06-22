'''
import numpy as np
with open ('B:\Example1.txt','r')as File1:
    file_stuff=File1.readline()

    print(File1.readline())
    print(File1.readline())
a=np.array([0,1,0,1,0])
b=np.array([1,0,1,0,1])
print(a*b)
'''
'''
class Points (object):
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def print_point(self):
        print('x=',self.x,' y=',self.y)

p2 = Points(1,2)
p2.x=2
p2.print_point()

print()
print()
''' # class
'''
import numpy as np
print(len(("disco",10)))

x=np.array([[3,3],[1,3]])
y=np.array([[3,1],[3,2]])

z=np.dot(x,y)
print(z)
''' #multiplic numpy

with open (example1,'R')as file 1:
