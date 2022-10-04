#<-------Functions with Inputs-------->
#Arguments and parameters in a function


#simple function
# def greet():
#     print("Hello")
#     print("How you doing")
#     print("What is the weather update?")

# greet()

#Function with input
# def greet_by_name(X):
#     print(f'Hello {X}')
#     print(f'{X}, How may i assist you?')

# name = input("What is you name?  ")

# greet_by_name(name)     #Here "X" is parameter and "name" is an argument---Aruguments is the actual data going to pass inside the function

#Functions with more than one input
def greet_with(name , location):
    print(f'Hello {name}, according to our records your loaction is {location}')

name_input = input("what is your name?  ")
location_input = input("please feed your location.  ")

# greet_with(name, location)              #these are the positional argumments

greet_with(location= location_input, name= name_input)                  #these are the keyword argument






