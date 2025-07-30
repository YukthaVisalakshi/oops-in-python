'''code to illustrate a product with its price by normal instance
and caluclate the product tax rate by 105 in a class method and print 
the total amount to be paid'''

class product:
    tax_rate=0.18
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def finalprice(self):
        total=self.price*(1+product.tax_rate)
        pribt(f"Final price of {self.name}is Rs.{total:.2f}")
    @classmethod
    def settax(cls,rate):
        cls.tax_rate=rate/100
name=str(input("Enter the product name:"))
price=float(input("Enter the base price:"))
rate=int(input("Enter tax_rate in %:"))
product.tax(rate)
item=product(name,price)
item.finalprice()
