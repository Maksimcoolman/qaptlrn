student = {
    "name": "alex",
    "grades": [5, 4, 5, 3, 4]
}

def average_grade(student):
    grades = student["grades"]
    return sum(grades) / len( grades)

print(f"{student['name']} average grade is: {average_grade(student)}")