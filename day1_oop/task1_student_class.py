# Task 1 — Student class:

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
    
s1 = Student("Shubham", 43, 85)
s2 = Student("Yash", 56, 95)

print(s1)
print(Student.college)

print(s1.get_grade())
print(s2.get_grade())