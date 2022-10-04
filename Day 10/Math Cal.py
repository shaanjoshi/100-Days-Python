import math
from art import logo
# print(logo)
def add(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def exp(num1, num2):
    return num1**num2
operations = { 
        "+" : add,
        "-" : subtraction,
        "*" : multiply,
        "/" : divide,
        "^" : exp
        

    }
def calculator():
    print(logo)
    N1 = float(input("Enter you first number: "))
    # operation_to_perform = input("+\n -\n *\n \ \nPick up an operation: ")
    should_continue = True

    while should_continue == True:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("What operation you want to perform from the above list? ")
        N2 = float(input("What's the next number? "))
        answer = operations[operations_symbol](N1, N2)

        print(f'{N1} {operations_symbol} {N2} = {answer}')

        user_continue = input(f"Type 'y' to continue with the {answer} or Type 'n' to start with the beginning: ")
        if user_continue == "y":
            should_continue == True
            N1 = answer
        elif user_continue == "n":
            should_continue = False
            calculator()
            # exit()

calculator()
    # operations_symbol = input("Pick another operation to perfom: ")
    # N3 = int(input("Enter the other number: "))

    # second_answer = operations[operations_symbol](first_answer, N3)

    # print(f'{first_answer} {operations_symbol} {N3} = {second_answer}')


