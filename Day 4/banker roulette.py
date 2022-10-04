import random
names_string = input("Give me everybody's names, separated by a comma. ")

names = names_string.split(", ")                            #storing given inputs in the array        

number_of_person = len(names)                            #storingf the lenght og the array or the total number of items in the list
random_choice = random.randint(0, number_of_person-1)    #this is the index numder of the random choice

random_person = names[random_choice]                        #for fetching the name of random person

print(f"{random_person} is going to buy the meal today! ")



#other way of doing above code simply by using choice() function
'''
random_person = random.choice(names)
print(f"{random_person} is going to buy the meal today! ")

'''



