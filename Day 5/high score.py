student_scores = input("Enter the scores of students: ").split()

for i in range (0,len(student_scores)):
    student_scores[i] = int(student_scores[i])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

