#<---------Functions with Ouputs---------->

def format_name(Fname, Lname):
    '''Takes first and last name and format it to return title case version of it '''
    if Fname == "" or Lname == "":
        return "You didn't provided the valid input"
    return Fname.capitalize() + " " + Lname.capitalize()

firstName = input("Enter you first name: ")
lastName = input("Enter your last name: ")

print(f'Your name is {format_name(firstName,lastName)}')

format_name
#docstring--- Means doing documentation - like what this function will going to perform

#-----DIffrence between print and return

#<------ While loop, flag and recursion ------->




