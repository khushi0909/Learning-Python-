
#* def somename():
#*     pass
#*  somename()



from math import exp


def somename(name,food="tacos"):        # food is having default value here and if food arg is not passed it will take this value 
    print(f"Hello {name},Lets eat some {food}")

somename("katty","pizza")

# answers:Hello katty,Lets eat some pizza

somename("kitta")
# Hello kitta,Lets eat some tacos

def somefunction():
    return "a value"

thing = somefunction()
print(thing)

# a value
#* in summary function is defined with the keyword name def,with unlimited parameters ,we can have default parameters

#TODO SCOPE
#* variables that live inside the function can simply be not accessed by the variable outside the fucntion

# def myfunc():
#     name ="kitu"
# print(name)

# error -name is not defined 

name ="anaya"           #* here it can look outside a funct for a variabl when inside func its not there 
def myfunc():
    return name 
print(myfunc())
#anaya

name ="atti"
def myfunc():
    name = "New Name"
    return name 

print(myfunc())
print(name)

# NewName  atti

#* its is always best practice to put your variable inside a argument and explicitly pass it in 

# def myfunc(name):