'''del method/class variable with const access'''
 
class abc():
    class_var=0
    print("Object variable:",class_var)
    def __init__(self,var):
        abc.class_var+=10
        self.var=var
        print("Object variable:",var)
        print("class variable", abc.class_var)
    def __del__(self):
        abc.class_var-=1
        print("obj var with %d is deleted" %self.var)
obj1=abc(11)
obj2=abc(12)
obj3=abc(13)
del obj1
del obj2
del obj3