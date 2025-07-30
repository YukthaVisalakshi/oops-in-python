def reverse_str(H):
    return H[::-1]
class Hasini:
    def __init__(self,val):
        self.val=val
    def display(self):
        print("Given value:",self.val)
    def modify(self):
        self.val=reverse_str(self.val)
n=input("Enter a string:")
o=Hasini(n)
o.display()
o.modify()
o.display()