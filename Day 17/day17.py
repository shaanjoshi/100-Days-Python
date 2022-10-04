#Creating Classes
'''
class User:     
    pass

user_1 = User()
user_1.id = "001"
user_1.username = "Shantanu"

print(user_1.username)
'''


#constructors in python
'''
Constructors are generally used for instantiating an object. The task of constructors is to 
initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the "__init__()" method is called the constructor and is always called when an object is created.
'''


#Example of "Self" argument and COnstructor
'''
class Employee:
    no_of_leaves = 8

    def __init__(self, Ename , Esalary, Erole): #Constructor--For instantiating an object
        self.name = Ename     #Here "self" is an object and "name", "salary", "role" they are the general parameters that you want to give to uour objects
        self.salary = Esalary
        self.role = Erole
        
    def printdetails(self):
        return 6*5
        return f"The name of the employee is {self.name} and his salary is {self.salary} and his role is {self.role}"

employee1 = Employee("Harry", 3456, "Insturctor")
# employee1.name = "Harry"
# employee1.salary = 3456
# employee1.role = "Insructor"
employee2 = Employee("Shaan", 7898, "Developor") 
# employee2.name = "Shaan"
# employee2.salary = 4567
# employee2.role = "Developor"

print(employee1.printdetails())
print(employee2.printdetails())
'''
#Another example

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):           #"Self in the function make sure that which object called that function"
        user.followers += 1           
        self.following += 1


user_1 = User( "001", "Jaani.patlu")
user_2 = User( "002", "shaanJoshi")

user_1.follow(user_2)

print(f"The {user_1.username} is having {user_1.followers} followers and following {user_1.following} people")
# print(user_1.following)

print(f"The {user_2.username} is having {user_2.followers} followers and following {user_2.following} people")
# print(user_2.following)


