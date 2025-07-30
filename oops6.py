class number:
    even=[]
    odd=[]
    def __init__(self,n):
        self.n=n
        if n%2==0:
            number.even.append(n)
        else:
            number.odd.append(n)
n1=number(21)
n1=number(33)
n1=number(32)
n1=number(38)
n1=number(53)
print("Even list:",number.even)
print("Odd list:",number.odd)