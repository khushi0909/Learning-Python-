#               <---PYTHON301-ADVANCE--->

# Creating first Python class ,Class Properties and Class Methods 

a Python class is a template, or constructor, used to create Python objects

“Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.”

Generally class name starts with upper case letter,and are accessed by dot annotation .


            class ThisIsAnimal:
                pass
            animal =ThisIsAnimal()
    
    
Benefit from the class because:

All your logic lives in a single function
It is easy to update and stays encapsulated
If you change anything later, you can easily keep the interface the same

_like_this="This is a private property"

any variable starting with underscore is private property and can be accessed ,only inside the class not outside the class

-----CLASS METHOD -----

it is a fancy name for a function inside a class.

A class method is a method that is bound to a class rather than its object. It doesn't require creation of a class instance, much like staticmethod. The difference between a static method and a class method is: Static method knows nothing about the class and just deals with the parameters.

[more information and live example of Python class,ClassProperties,ClassMethods](first_class.py)

# CLASS INHERITANCE and CLASS INTERFACES and CLASS SUPER() METHOD

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

        ---class interface ---
it is literally a blueprint
an interface acts as a blueprint for designing classes. Like classes, interfaces define methods. Unlike classes, these methods are abstract. An abstract method is one that the interface simply defines. It doesn’t implement the methods. This is done by classes, which then implement the interface and give concrete meaning to the interface’s abstract methods.

        ---CLass SUPER() METHOD ---

 now we we write its own method in inherited class that has same name in main class i.e parent class ,preference is given to method of a inherited class and is executed ,but what if we want to execute methods of both parent and inherited class (they have same name) .Here super method comes in to play 

 [More Info and examples of Inheritance,Interface ans SuperMethod](class_inheritance_n_Supermethod_n_interface.py)

 # DUNDER METHODS 

 dunder = double underscore 
 These are the magic method that comes with the class 
 methods with _INIT_ are initiated first in order for parent and inheritated class .

[info and example](dunder_method.py)

# Error Exception ans Catching Exception

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal

There are different type of exceptions built in 

https://docs.python.org/3/library/exceptions.html#bltin-exceptions

[info and example](error_exception.py)

# PYTHON DECORATORS 

simply a fucn that wraps around other functon 

Now, why would we ever do this?

Well, because sometimes we have a function and we simply like what it's doing and we just simply want

to add a little extra logic to it, a little extra functionality.

And so we don't necessarily always want to change our original function, but maybe we do want to take

that original function and extend it.

So it's a lot like class inheritance where we took a regular class and we inherited it into a new class

or extended it into a new class.

This is taking a function and extending it with my decorator.

Now, this is a very, very, very simple decorator, but it gets the example across.


there are two ways to call decorator or do things ,check example
[info and example](decorators.py)

# PYTHON GENERATORS 

Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

[example and more imp infos](generators.py)

# USING PIPENV FOR A VIRTUAL ENVIRONMENT

previously we did with pythom -m venv .venv ...... cmd 

but there is another way to do it i.e ## pipiens

    pip install pipenv

    pipenv

it will give list of cmd ,this is easier method 

    pipenv install

    pipenv shell

now you are inside virtual env becoz it has () OR SOMETHING

    python _V

    hit  Ctrl + D (to logout)

To get rid of pipenv

    pipenv --rm


