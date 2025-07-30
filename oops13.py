'''Mutable type attributes
code to illustrate multiple attributes by calling a class fpr its specifications
for example n=21,32,43,54,65
even list:[32,54]
odd list:[21,43,65]'''

class number:
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.evens.append(num)
        else:
            number.odds.append(num)
        
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print("Even Mutable list:",number.evens)
print("Odd Mutable list:",number.odds)

