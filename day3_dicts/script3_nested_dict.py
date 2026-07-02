# Script 3 — Nested dictionary:
# Create a nested dictionary of 3 students, each with name, age, and marks. Write a loop that prints each student's full info.

students = {
    "student1": {
       "name" : "Shubham",
       "age" : 23,
       "marks" : 85
    },
    "student2": {
        "name" : "Adarsh",
        "age"  : 21,
        "marks" : 75
    },
    "student3": {
        "name" : "Yash",
        "age"  : 21,
        "marks" : 95
    }
}

for student, info in students.items():
    print(student)
    print("Name:",info["name"])
    print("Age:",info["age"])
    print("Marks:",info["marks"])
    print()