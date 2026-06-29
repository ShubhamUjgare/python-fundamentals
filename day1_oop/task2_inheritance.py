# Task 2 — Inheritance:

class Student:

    college = "Pune University"

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def get_grade(self):
        if self.marks > 90 and self.marks <= 100:
            return 'A'
        elif self.marks > 80 and self.marks <=90:
            return 'B'
        elif self.marks > 70 and self.marks <= 80:
            return 'C'
        else:
            return 'F'

    def __str__(self):
        return f"Student({self.name}, Roll No: {self.roll_no}, Marks: {self.marks})"
    
class EngineeringStudent(Student):

    def __init__(self, name, roll_no, marks, branch, year):
        super().__init__(name, roll_no, marks)
        self.branch = branch
        self.year = year

    def show_full_info(self):
        print(f"Student({self.name}, Roll No: {self.roll_no}, marks: {self.marks}, grade: {self.get_grade()}, Branch: {self.branch}, Year: {self.year}")

    def __str__(self):
        return f"Student(Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks})"

e1 = EngineeringStudent("Shubham", 43, 85, "Computer Engineering", 3)
print(e1)

e1.show_full_info()
print(e1.college)