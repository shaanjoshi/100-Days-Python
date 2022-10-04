#Understanding OOPs in Python
'''
We use OOPs to split larger task into a smaller pieces, so that it can be reuse in the future

It's not easy to build a larger or acomplex program by using prodedural programming so we use OOPs

'''

'''
Taking an example of self driving car:
** Components needed in the self driving car **
1. Camera module of object detection
2. Lane Detection module
3. Map module
4. Fuel management

'''


#How to use OOPs

'''
Lets just build a virtual resturant:
Employee need to hired is:

1. Waiter(Class) :
***********

Has:            #---Attributes--- It just a variable that is associated with are class(waiter).
    is_holding_plate = True
    table_resposible = [4,5,6]

Does:           #---Methods--- It is just a function that can be performed by our class(waiter).
    def take_order(table, order):
        #takes order to chef
    def take_payment(amount):
        #add money to resturant


So in our resturant there will be more than one waiter lets say:
1. Henry(waiter1)
2. Betty(waiter2)

So here waiter will be the claas and Henry and Betty are the objects associated with the "waiter" class
therefore, the "Class" can be reffered as the blue print for the "object"


****
2.Simalry a class can be made for the  receptionist
3.Simalry a class can be made for the cook
'''

#Consturcting objects 
'''
car = carBlueprint()

Here, car is the Object created from the Class named blue print

'''

#Accessing attributes and methods
'''
car.speed()         #acessing the speed attribute and here car is the object
car.stop()          #calling function "stop" 
'''

#Python Packages
'''
The Python Package Index (PyPI) is a repository of software for the Python programming language.
PyPI helps you find and install software developed and shared by the Python community.
'''

#Modifying object attributes and calling methods
