def my_decorator(func):
    def wrapper():
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper

@my_decorator
def myfunc():
    print("My name is Kalob")
#^ 1st way to call decorator
# myfunc()
# ^ here myfunc function is thown inside my_decorator as a function not as a variable 

# Do something here
# My name is Kalob
# Original function is finished

#^ second way to call decorator 
def myfunc():
    print("My name is Kalob")

def my_decorator(func):
    def wrapper():
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper

new_func = my_decorator(myfunc)
new_func()
