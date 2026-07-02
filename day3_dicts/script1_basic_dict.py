# Script 1 — Basic dict operations:
# Create a dictionary of 5 students with name and marks. Add a new student. Update one student's marks. Delete one student.

students = {
    "Shubham" : 75,
    "Yash" : 85,
    "Adarsh" : 65,
    "Harsh" : 78,
    "Sahil" : 93
}

# Add a new student
students["Rushi"] = 53
print(students)

# Update one student's marks
students["Yash"] = 65
print(students)

# Delete one student
students.pop("Adarsh")

# updated students dict 
print("Updated students dictionary: ",students)