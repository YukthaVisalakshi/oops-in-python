import math
class SquareRoot:
    def __init__(self,num):
        self.num=num 
    def find_root(self):
        return math.sqrt(self.num)
num=float(input("Enter the number"))
s=SquareRoot(num)
print(f" squareroot: {s.find_root():.2f}")