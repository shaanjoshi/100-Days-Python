#scope- Local and Global
enemies = 1                                 #globally defined / global scope can be used inside as well as outside the functions also
def increase_enemies():
    enemies = 2                             #locally defined / local scope - can be used inside the funcion only
    print(f"enemies inside the function is {enemies}")

increase_enemies()
print(f"enemies outside the fuction is {enemies}")



def game():         
    def cricket():              #example of nested function whuich is defined locally inside other function
        batsman = "sachin"
        print(batsman)

'''
Block Level Scope: This scope restricts the variable that is declared inside a specific block, from access by
the outside of the block. 
'''
#Also there is no block scope in python language. For ex:-
score =  5
player = ["a", "b", "c"]
if score < 5:
    new_player = player[0]
print(new_player)            #this line won't give any error since there is no block scope



#How to modify a global variable in side a function

a = 1
def modify():
    global a       #We need to mention inside the function that there is somewhere a global variable outside a function which needs to modify  
    a =+ 1

#Python constant and global scope

#global constant. Ex:-

PI = 3.14768        #always declare constant variable in upper case
URL = "http//www.mywebsite.co.in"

#Number guessing game



