sum = 0
for number in range(0,101,2):
    sum += number
print(sum)
sum2 = 0
for number in range(1,101):
    if number %2  == 0:
        sum2 += number
print(sum2)
   