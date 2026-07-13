student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for keys in student_scores:
    score = student_scores[keys]
    if score >= 91:
        student_grades[keys] = "Outstanding"
    elif score >= 81:
        student_grades[keys] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"
print(student_grades)