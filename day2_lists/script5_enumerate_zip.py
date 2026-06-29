# Script 5: Use enumerate and zip together — given two lists of names and scores, print "Rank 1: Rahul — 95" format for all students sorted by score descending.

names = ["Shubham","Yash", "Adarsh"]
scores = [95,75,85]


students = zip(names, scores)
students = list(students)
students.sort(key=lambda x : -x[1])

for rank, student in enumerate(students,start=1):
    name,mark = student
    print("Rank",rank,":",name,"-",mark)
