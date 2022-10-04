#control flow with if /else and conditional operators
print("Welcome to rollercoaster")
height = int(input("Enter your height in centimeter:  "))
bill = 0
if height >= 120:
    print("woohoo! Your are allowed to take ride")
    age = int(input("Enter your age: "))
    if age < 10:    
        bill = 7                                       #nested if statement
        print("You need to pay 7$ for ride")
    elif age <= 18:
        bill = 4
        print("you need to pay 4$ for ride")
    elif age >=45 and age <= 55:
        bill = 0 
        print("Evrythimg is gonna be okay! Ride is on us. ")
    else: 
        bill = 12
        print("adult ticket are of 12$")
    
    photo = input("Do you want a photo taken? yes or no: ")
    if photo == "yes":                                 #multiple if statement     
        #add 3$ to bill
        bill = bill + 3
        print(f"Your total bill is {bill}$. Thankyou! ")
    else:
        print(f"Your total bill is {bill}$. Thankyou! ")
    
else:
    print("You are not allowed to take ride")

#nested if statement and elif statement

#multiple if statements

#count() and lower() function 
a = "Shaan"
print(a.count("a"))
print(a.lower())




