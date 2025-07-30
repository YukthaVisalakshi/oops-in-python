class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1:",self.var1)
        print("var2:",self.var2)
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
o=abc(n1,n2)
print("Object.__dict__ - ",o.__dict__)
print("Object.__doc__ - ",o.__doc__)
print("Object.__name__ - ",abc.__name__)
print("Object.__module__ - ",o.__module__)
print("Object.__base__ - ",abc.__base__)
