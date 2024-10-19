# Ask user for number of completed quizzes & labs
number_labs_completed = int(input("Enter the number of labs completed: "))
number_quizzes_completed = int(input("Enter the number of quizzes completed: "))

# Calculate weighted grade based on number of completed labs, 6 or more = full marks
if number_labs_completed >= 6:
    labs_weighted_grade = 20
else:
    labs_weighted_grade = (number_labs_completed/6)*20

# Calculate weighted grade based on number of completed quizzes, 6 or more = full marks
if number_quizzes_completed >= 6:
    quizzes_weighted_grade = 15
else:
    quizzes_weighted_grade = (number_quizzes_completed/6)*15

# Prompt user for grades and sum all weighted grades into a single overall grade
overall_grade = 0
overall_grade += labs_weighted_grade
overall_grade += quizzes_weighted_grade
overall_grade += (int(input("Enter grade for Assignment 1: ")) * 0.04)
overall_grade += (int(input("Enter grade for Assignment 2: ")) * 0.04)
overall_grade += (int(input("Enter grade for Assignment 3: ")) * 0.04)
overall_grade += (int(input("Enter grade for Assignment 4: ")) * 0.04)
overall_grade += (int(input("Enter grade for Midterm 1: ")) * 0.125)
overall_grade += (int(input("Enter grade for Midterm 2: ")) * 0.125)
overall_grade += (int(input("Enter grade for Final Exam: ")) * 0.18)
overall_grade += (int(input("Enter grade for Midterms and Final Preparation: ")) * 0.06)

# Display overall grade
print("Your grade is: " + str(round(overall_grade, 2)))