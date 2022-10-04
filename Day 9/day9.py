# #Dictionary
# #Nesting in dictionary and list and both 

# #<------Dictionary in python------>
'''
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    
    }
'''
# print(programming_dictionary["Bug"]) #Retriving items in dictionary

# programming_dictionary["Loop"] = "An action of doing something again and again" #adding new key and value to the dictionary


# # print(programming_dictionary)

# empty_dic = {}      #Empty dictionary

# # #wiping a existing dictionary
# # programming_dictionary= {}

# #redefining key
# programming_dictionary["Bug"] = "The new content"

# print(programming_dictionary)

# #looping through a dictionary
'''
for key in programming_dictionary:
    print(key)                          #it will print the key
    print(programming_dictionary[key])  #it will print the values of those key
'''


# #<-------Nesting------->
'''
capitals ={
    "France" : "paris",
    "Germany" : "berlin"
}
'''
# # Nesting list inside dictionary
'''
travel_log = {
    "France" : ["paris", "lille", "dijon"],
    "Germany" : ["berlin", "hamburg", "stuttagart"]

}
'''
# # Nesting dictionary in a dictionary
'''
travel_log = {
    "France" : {"cities_visited": ["paris", "lille", "dijon"], "total_visit" : 12},
    "Germany" : {"cities_visited": ["berlin", "hamburg", "stuttagart"], "total_visit": 8}


}
'''

# Nesting dictionary inside list
'''
travel_log = [
    {
        "Country": "France", 
        "cities_visited": ["paris", "lille", "dijon"],
        "total_visit" : 12
    },
    {
    "Country": "Germany",
    "cities_visited": ["berlin", "hamburg", "stuttagart"],
    "total_visit": 8
    }


]
 
for i in range(0,len(travel_log)):
    print(travel_log[i])
'''
#Quiz question: print the output "Steak"

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])


