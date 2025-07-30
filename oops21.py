class ATM:
    def __init__(self):
        self.pin = "user1234"
        self.balance = 5999

    def access(self):
        if input("Enter PIN: ") != self.pin:
            print("Wrong PIN"); return
        print("Access granted")
        op = input("Enter withdraw: ")
        if op == 'w' and self.balance >= 2000:
            self.balance -= 2000
            print("₹2000 withdrawn\nRemaining balance: ₹", self.balance)
        elif op == 'd':
            amt = int(input("Enter amount to deposit: "))
            self.balance += amt
            print(f"₹{amt} deposited\nNew balance: ₹{self.balance}")
        else:
            print("insufficient balance")

ATM().access()
