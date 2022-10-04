#Randomisation/ Random modules
#mersenne twister

'''
- middle squares method - method for randomaization - to generate long line number - psedorandom number genetor
- Diffrence between randomly generated and pseudorandomply generated number
 * security increases as length of seed increases
 * 
'''

# import random             #python module to generate pseudorandom nnumber
# random_int = random.randint(23,67)
# print(random_int)

'''
A Python module is a file containing Python definitions and statements. 
A module can define functions, classes, and variables. A module can also include runnable code. 
Grouping related code into a module makes the code easier to understand and use. 
It also makes the code logically organized.
'''

'''
import my_module            #userdefined python module
print(my_module.pi)        
'''
# random_float = random.random()
# random_float * 7897
# print(random_float)




#Lists(array)
'''
#its a data structure of storing and organising data in python

states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
"Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
"Odisha", "Punjab", "Rajasthan", "Sikkim", "West Bengal", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand"]

states_of_india.append("new1")              #to add item in the list from last index of the list
states_of_india.extend(["new2", "new3", "new4", "new5"])            #to add bunch of items to add multiple elements to the list or by extending the list 
states_of_india.insert(4, "new7")           #to add item a particular index number  
states_of_india.remove("new1")              #to remove the particular item from the list
states_of_india.pop(-2)                     #to remove the element at that particular index number
print(states_of_india.count("new5"))        #gives the count of the element in the list

print(states_of_india)

'''

# Methods of converting a string to list in Python
'''
str = "ram, sham, dham"

print(str.split(", "))      #split() function splits the string and store it in the form of array or list

'''

#Nested list

list1 = ["A", "B", "C", "D", "E"]
list2 =  [1, 2, 3, 4, 6, 7]

nested_list = [list1, list2]

print(nested_list)
print(nested_list[1][1])