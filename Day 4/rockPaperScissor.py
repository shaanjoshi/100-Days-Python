import random
rock = '''
    _______
---'   _____)
      (______)
      (__R___)
      (_____)
---.__(____)
'''

paper = '''
    _______
---'   ____)____
          ______)
          ___P____)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       ____S______)
      (____)
---.__(___)
'''

compOptions = [rock, paper, scissors]

# print(compOptions)
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if userInput >= 3 or userInput < 0: 
    print("You typed an invalid number, you lose!")
else:
    print(f'you have choose: {compOptions[userInput]}')

    compChoice = random.randint(0,2)
    
    random_ans = compOptions[compChoice]
    print("Computer's choice is :\n"  )
    print(random_ans)

    # if userInput >= 3 and userInput < 0: 
    #   print("You typed an invalid number, you lose!")

    if userInput == compChoice:
        print("It's a tie")
    elif userInput == 0 and compChoice == 1:
        print("You Lose")
    elif userInput == 0 and compChoice == 2:
        print("You Win")
    elif userInput == 1 and compChoice == 0:
        print("You win")
    elif userInput == 1 and compChoice == 2:
        print("You lose")
    elif userInput == 2 and compChoice == 0:
        print("You Lose")
    elif userInput == 2 and compChoice == 1:
        print("You Win")
