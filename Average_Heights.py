Fruits = ["Apple", "Guava", "Mangoes"]
for i in Fruits:
  print(i)

student_heights = input("Input a list of student heights ").split(',') 
for n in range(0, len(student_heights)):
  student_heights[n] = float(student_heights[n])

print(student_heights)
print(n)
total_heights = 0
for n in range(0, len(student_heights)):
    total_heights = total_heights + student_heights[n]
    print(f"Total Heights: {total_heights}")

average_heights = round(total_heights / (n + 1))
print(f"Average heights of entered {n+1} studendts is: {average_heights}")
