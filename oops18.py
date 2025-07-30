'''code to view the memory info in a class,which 
gives the type of the class,size of the class object,
and size of instance
const: use package-sys for size of
given value of num=10
class A:'''

import sys

class A:
    def __init__(self, num):
        self.num = num
obj = A(10)
print("Type of the class:", type(A))
print("Size of class object:", sys.getsizeof(A))
print("Size of instance:", sys.getsizeof(obj))
print("Size of instance variable 'num':", sys.getsizeof(obj.num))
