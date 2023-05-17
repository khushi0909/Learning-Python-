can_code = True
if can_code == True:                    # here we can also do as if can_code (it will take it as if can_code is true ,instead of writing comparison operator ==)
#do a thing 
    print("you can code ")
else:
# do something else 
    print("you dont know to code yet ")

# 2nd 
    name = input("what os your name ")

    if name == "Bob":
        print("Welcome Bob!")
        bring_food = "pizza"
    elif name=="Kalob":
        print("welcome to your teacher portal")
        bring_food = "Tacos"

    else:
        print("You are not bob get outta here ")
        bring_food = "Salmon"

    print(f"you are eating {bring_food}")

#3rd

name = input("What is your name ")
name = name.lower()

if name!= "bob":
    print("You are not bob ,get out of here ")
else:
    print("Welcome Bobby boy ")

    # 4th

    age =18
    if age<18:
        print("not allowed to vote ")

        #* >   greater than
        #*  >=    (greater than euql to)
        #* <    (less than)
        #* <=    (its less than equal to)
        #* ==    (its same as )
        # !=        (not the same )      (all these are operators for comparison)

        #TODO MUTLIPLE COMPARISION OPERATOR

        age = 31
        name = "Kalob"

        if age >= 18:
                if name == "Kalob":
                        print("I can drink alcohol")


    #* or it can be done as 

    if age >= 18 and name == "Kalob":   #  if age >= 18 or name == "Kalob"      (or can also be used )
                      print("I can drink alcohol")
             
    #* with and both conditions needs to be true and with or only one condition needs to be true