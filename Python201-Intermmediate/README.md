# WELCOME TO PYTHON 201 !!!!

# INOperator :

In Python, the in operator determines whether a given value is a constituent element of a sequence such as a string, array, list, or tuple. When used in a condition, the statement returns a Boolean result of True or False. The statement returns True if the specified value is found within the sequence

[python file for IN Operator](INOperator.py)

# NOT Operator :

It is used to get the negation of a value, i.e. it allows us to invert the truth value of a given boolean expression. This operator can be applied in boolean situations like if statements and while loops. It also functions in non-Boolean settings, enabling you to reverse the variables’ truth values.

The below table shows the outcomes for some input values when the not the operator is applied to them.

Input	Output
True	False
False	True
not is a unary operator which means it takes only one input value. It can be used with any boolean expression or Python object.

[Python file for NOT Operator](NOTOperator.py)
# How to read files with Python 

we open files in a python with something called as a context manager .it is memory performant way .

syntax is:

     with open('filename','r') as file:          /// r stand for read 
     print(file.read())

[file try for reading and more info](reading_files.py)

# How to create files and writing with python 

we can create a new file through py and then write on it line by line 

[file to see how ,for creating and writing in the file](writing_files.py)

# Reading multiple linea from a file 

if soemone gives you a list of 100 emails and wanted you to find the one that has specific name in it ,how are we going to do that??THis islot like scrapping the data from the internet which is a very very common thing 

[try seeing with example here](reading_multiple_lines.py)

# Writing a File and Executing it 

Idea here is that you can ask a user for some form of input and then you can create a file out of that and with that file you can add some content in there as well

so it will be mergin all the experience that we have done till now with reading and writing and appending files in to a program,where you can basically create your own form of the catalaouge or contact book or a addrress book 

[writing file and Executing examples](executable_user_files.py)

#   Functions inside of functions (Nested Functions)

In pyhton everything is called an object and that means fucntions and sort of functions are objects,files are objects,packages are objects.Everythign is an object 

we will the see the scope and how it affects the functions inside of functions.

Here comes the term decorator .

In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.

[nested_func_scope example](nested_func_scope.py)

# Making a simple API Request 

We will be needing to use a package called requests

    >>>python
    >>>import requests

if you see n error ,then you are good to go ,nut if you module not found error then you have to go and install it ,quit() from shell and you are going to need to have a PIP now ,you should already have pip installed on your computer

    pip -V 
you will see some things including the version 

Now, if this cmd dosent work ,go and see the lesson how to install pip or google it 

Now do 

    pip install requests

Now, you can import requests on the files 

What is PIP?
PIP is a package manager for Python packages, or modules

What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

[example of gow to do](simple_api_requests.py)

# Making a JSON API request 

We will just get some info,we are not going to post any info or put or delete or any other API term .

its same as making normal request but if data turns out to be JSON ,we need to do varname.json()

and the we have accessto the data 

[example of JSON API Fetching](making_json_ap_requests.py)

# Reading JSON and editing JSON 

last time our data came back as json or dictionary  and was fine and workable ,what if it comes back as a string ,and format that is not a dictionary ,so to get data you cannot do simply person['name] ,it will give error as indices must be integers and thats because its trying to slice other data types such as strings ,so it doent have a property or key called name 

so we need to convert that and it could be done with json library 

        import json

[example can be seen and executed](reading_json.py)

# Function *args and **kwargs

Nice thing is you can pass in here an unlimited number of arguments and it will just work 

1) The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function

2) What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).

3) For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together. It can be done using *args.

4) Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.

5) IMP: it always comes back as tuple data type 

<---------------KWARGS------------>

1) kwargs are with two ** and always comes back as a dictionary datatype because keyword looks something like thing:'something'

2)  **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list

3)We use the name kwargs with the double star. The reason is that the double star allows us to pass through keyword arguments (and any number of them).

4) A keyword argument is where you provide a name to the variable as you pass it into the function.

5) One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

[example of *args and **kwargs as follows](func_args_kwargs.py)







