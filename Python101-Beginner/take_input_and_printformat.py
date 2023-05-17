# *
#* lets say you want to make cmd line game or you want to accept some sort of user input*,you need to use input()

# * anytime you ask for input it will coem back as string even if you ask for a number 


age = input("what is your age ")
dog_years = age*7
print(dog_years)

# answer is : what is your age 90
# 90909090909090

#* here input was 90 bu it printed multiple times because it is accepting it as a string and here comes typecasting ,but if i accept the input any name or any other string it will work fine

#TODO TYPE CASTING 

#* any data type can be changed to other data type
ager = input("what is your age")
data_type = type(ager)

print(data_type)

ager = int(ager)
data_type = type(ager)
print(data_type)


# answer is:  what is your age 21
# 21212121212121
# what is your age21 
# <class 'str'>
# <class 'int'>

grocery_list = ["Apples","oranges","banana","Apples"]
grocery_list= set(grocery_list)         #* casting it here to be a set 
print(grocery_list)
print(type(grocery_list))

# answer is : {'oranges', 'Apples', 'banana'}           (so its unique ,no twice apples ,doid you notice )
# <class 'set'>

#TODO Print Formating 

#* many different ways to format ,but we will see here only two 
#* .format
#* fstring


welcome_message = "Hello_____ welcome to python 1010"
print(welcome_message)

# we need to somehow replace the ____

name = "kirti"
welcome_message = "Hello {} welcome to python 1010".format(name)

print(welcome_message)

# this will for this curly braces and then it is going to format it with .name 

# answer is : Hello kirti welcome to python 1010
#*2nd method -preffered way 
name = "kirti"
welcome_message =f"Hello {name} welcome to python 1010"

print(welcome_message)
#* 3rd way -this is the old way of doing it 
welcome_message = "Hello %s welcome to python 1010"%name
print(welcome_message)
#%s --- says it is somekind of string 




