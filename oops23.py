class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def input(cls):
        name=str(input("Enter the name:"))
        marks=int(input("Enter the marks:"))
        return cls(name,marks)
    def display(self):
        print(f"student name: {self.name}")
        print(f"student marks: {self.marks}")
s= student.input()
s.display()