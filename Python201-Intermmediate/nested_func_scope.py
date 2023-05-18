def thing1():
    print("Welcome to thing 1 ")

    def thing2():
        print("Welcome to thing 2")
    thing2()

#^ so here are two fucntions and here only required is to call one or execute one 

thing1()

#^ thing 1 we know it is a regular function ,thing2 is going to register o be registered inside of thing1 and then we executed it 
#^ so this is the func inside the func and ultimately that is what is called a decorator 

#^ so if we look at the scope 

def thing3(name):
        print("Welcome to thing 3 ",name)

        def thing4(name):
            print("Welcome to thing 4",name)
        thing4(name)

thing3("Jacob")

#answer: 
# Welcome to thing 1 
# Welcome to thing 2
# Welcome to thing 3  Jacob
# Welcome to thing 4 Jacob

#^ her passing the name along and having to type same variable over and over again is irritating to see how many times i have to type above 

#^ The nice thing about the pythonic scoping is that if it doesnt find the name inside a function ,suppose in thing4 ,this is going to look outside of a fucn 
#^ its going to look in the thing3 for a variable called name,so the thing4 is going o say welcome to thing4,its going to have name in ther e but we are not passign anything 
def thing3(name):
        print("Welcome to thing 3 ",name)

        def thing4():
            print("Welcome to thing 4",name)
        thing4()

thing3("Jacob")

# answer 
# Welcome to thing 3  Jacob
# Welcome to thing 4 Jacob

#^ ere even though we didnt pass ine explicitly the name parameter,what it did was look for a name inside thing4 ,it didnt find it and looked inside thing3 and found and printed ,this is scope 
#^ so if i try to print name outside function scope ,it wil trow an error 

# print(name)