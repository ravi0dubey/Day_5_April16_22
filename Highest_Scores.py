
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
a = 0

for n in range(0,len(student_scores)):
    a = student_scores[n]
    if (a > highest_score):
        highest_score  = a

print(f"The highest score in the class is : {highest_score}")
#print(max(student_heights)) This will give Maximum value of the list
#print(min(student_heights)) This will give Minimum value of the list
