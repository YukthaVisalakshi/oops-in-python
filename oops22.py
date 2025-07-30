class student:
    def __init__(s,name,marks):
         s.name=name
         s.marks=marks
    def display(self):
        print(f"student name:{s.name}")
        print(f"student marks:{s.marks}")
name=str(input("Enter the name:"))
marks=int(input("Enter the marks:"))
s=student(name,marks)
s.display()