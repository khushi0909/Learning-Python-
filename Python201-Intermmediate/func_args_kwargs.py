# def thing(name,*args):
    # *args

#^ here it doesnt have to be args it just have to start with * and name can be anything else 

    #^ what data type does this look like to you ? you should be saying its like a tuple and thats what ARGs comes back as ,it always comes back as a tuple and we can loop through the data as tuple

def add_numbers(*args):
    print(args)
    total = 0
    for num in args:
        total = total + num 
    return total 

total = add_numbers(1,3,5,7,9)
print(total)


# answer:(1, 3, 5, 7, 9)
# 25

def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

person(name = "jacob",age =27,brain ="Huge")

# {'name': 'jacob', 'age': 27, 'brain': 'Huge'}
# <class 'dict'>

def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("You age is ", kwargs.get("age"),kwargs["name"])

person(name = "jacob",age =27,brain ="Huge")

# You age is  27 jacob

#^ let s say you want to order pizza from a website and for every topping we want to add 2 $

def order_pizza(name,address,**toppings):
    print(f"Order is for {name}")
    print(f"Ship it to {address}")
    price = 18.00
    for key,value in toppings.items():
        price =price + 2.00
    print(f"The total price is {price}")
    return price 

order_pizza("Amanda","cananda",jalapenos= True,extra_cheese = True,ham=True)

# Order is for Amanda
# Ship it to cananda
# The total price is 24.0