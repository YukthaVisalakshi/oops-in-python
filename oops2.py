class abc:
    def __init__(self,value):
        print("This is a class method")
        self.value=value
        print("Accessed value in class is ", value)
num=int(input("Enter a value:"))
obj=abc(num)