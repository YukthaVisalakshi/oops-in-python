class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Calc obj created.......")
    def add(self):
       return self.a+self.b
    def sub(self):
        return self.a-self.b
    def __del__(self):
        print("Created Calc obj was deleted")
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=calc(a,b)
print("Addition:",c.add())
print("subtract:",c.sub())
del calc

