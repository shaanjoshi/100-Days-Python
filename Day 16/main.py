'''
from turtle import Turtle, Screen      #Importing "Turtle" class and "Screen" class from "turtle module"

timmy = Turtle()                #Creating the object name timmy from Turtle class
shaan = Turtle()
print(timmy)                    #It will print the info about the timmy and where it is stored in th memory
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
shaan.backward(100)
my_screen = Screen()            #created the object name "my_screen" from "Screen" class
print(my_screen.canvheight)            #using "cavheigth" arrtribute fot "my_screen" object

my_screen.exitonclick()

'''


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

table.align = "l"           #modifying object attributes 
print(table)





