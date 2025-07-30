class student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def hi(self):
        print(f"Hello,I am {self.name} and i am {self.age} years-old. i am {self.gender}")
s=student('Amulya',32,'Male')
s.hi()