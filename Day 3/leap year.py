#nested if statements
year = int(input("Enter the year you want to know about  "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else: 
    print("Not leap year.")
