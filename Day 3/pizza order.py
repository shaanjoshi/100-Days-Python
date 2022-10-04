print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

amt = 0

if size == "S":
    amt += 15
elif size == "M":
    amt += 20
elif size == "L":
    amt += 25

if add_pepperoni == "Y":
    if size == "S":
        amt += 2
    elif size == "M" or "L":
        amt += 3
if extra_cheese == "Y":
    amt += 1
else:
    amt += 0
print(f'Your final bill is ${amt}')