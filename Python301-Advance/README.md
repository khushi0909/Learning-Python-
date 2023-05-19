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