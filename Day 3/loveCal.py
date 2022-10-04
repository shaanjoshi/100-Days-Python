print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

N1 = name1.lower()
N2 = name2.lower()

N = N1 + N2
# print(N)

trueCount = str(N.count("t") + N.count("r") + N.count("u") + N.count("e"))
#print(trueCount)
# print(type(trueCount))
loveCount = str(N.count("l") + N.count("o") + N.count("v") + N.count("e"))

totalPer = int(trueCount + loveCount)

if totalPer < 10 or totalPer>90:
    print(f"Your score is {totalPer}, you go together like coke and mentos.")
elif 40 <= totalPer <= 50:
    print(f"Your score is {totalPer}, you are alright together.")
else:
    print(f"Your score is {totalPer}.")
