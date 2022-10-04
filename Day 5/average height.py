
student_heights = input("Input a list of student heights ").split()
# print(type(student_heights))
# print(student_heights[0] + student_heights[1])
for n in range(0, len(student_heights)):                            #for loop to change the datatype of elements of the list
  student_heights[n] = int(student_heights[n])


# #Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height
avg = round(total_height/len(student_heights))

print(avg)

#otherway of doing the avbove question
'''
sum = sum(student_heights)
avg = sum/ len(student_heights)

print(avg)

'''
