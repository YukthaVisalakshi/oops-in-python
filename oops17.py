def reverse_str(H):
    return H[::-1]

class abc():
    def __init__(self,val):
        self.val=val
    def display(self):
        print("Given value:",self.val)
    def modify(self):
        self.val=reverse_str(self.val.upper())
n=input("Enter the string:")
o=abc(n)
o.display()
o.modify()
o.display()