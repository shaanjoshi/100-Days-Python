#Hurdles loop challenge
'''
#hurdle 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def full_cir():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# for i in range(0,6):                  #using for loop
#  full_cir()

number_of_full_cir = 6                  #using while loop
while number_of_full_cir >0:
    full_cir()
    number_of_full_cir -= 1



'''

#While loop

'''
#Hurdle 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def full_cir():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    full_cir()

'''
'''
#Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def full_cir():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        full_cir()
    else:
        move()


'''

'''
#Hurdle 4 (Variable Height)
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
        
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

'''

'''
#Maze(Need to go to the video after the completion of day 15)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        move()



'''
