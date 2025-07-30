'''create a class atm and check the pin user1234
define a function to withdraw 2000/-, balence amount from
account 5999, if the amount is over the balence exit and check the
pincode for accessing the account'''


class ATM:
    def __init__(self):
        self.pin = "1234"
        self.balance = 5999
    def access(self):
        if input("Enter PIN: ") == self.pin:
            print("Access granted")
            if self.balance >= 2000:
                self.balance -= 2000
                print("₹2000 withdrawn")
                print("Remaining balance: ₹", self.balance)
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")
ATM().access()